import cv2

KEY_ENUM = {27:"KEY_ESC",115:"KEY_s",97:"KEY_a", 100:"KEY_d"}


class Capture:
    def __init__(self, windName = "视频捕捉窗口", Path = str):
        self.frameNum = 0
        self.isPlaying = False
        self.windowName = windName
        self.cap = cv2.VideoCapture(windName)
        self.path = VideoPath
        self.func = None

        # self.draw_box = [0,0,0,0]
    def set_process_func(self, func):
        self.func = func


    # def callback_mouse(self, event, x, y, flags, param):
    #     pass

    def callback_bar(self, pos):
        None

    def process_img(self, img):
        img_dst = self.func(img)
        cv2.imshow(self.windowName, img_dst)
        pass


    def startProcessing(self):
        #加载视频
        total_frames = self.cap.get(cv2.CAP_PROP_FRAME_COUNT)
        # 定义窗口和鼠标回调
        cv2.namedWindow(self.windowName)
        # cv2.setMouseCallback(self.windowName, self.callback_mouse)
        cv2.createTrackbar('frames:', self.windowName, 0, int(total_frames), self.callback_bar)
        self.isPlaying = True

        while True:
            trackPos = cv2.getTrackbarPos('frames:', self.windowName)
            #如果暂停了
            if self.isPlaying:
                # 进度条与帧数一致
                if self.cap.get(cv2.CAP_PROP_POS_FRAMES) == trackPos:

                    cv2.setTrackbarPos("frames:", self.windowName, trackPos+1)

                # 进度条与帧数不一致
                else:
                    self.cap.set(cv2.CAP_PROP_POS_FRAMES, trackPos)

                # 读取指定的帧
                ret, img = self.cap.read()
                cv2.setTrackbarPos("frames:",self.windowName, trackPos+1)
                # cv2.imshow(self.windowName, img)
                self.process_img(img)

            key = cv2.waitKey(30)
            if key in KEY_ENUM:
                if 27 == key:
                    break
                else:
                    # 按下暂停s
                    if 115 == key:
                        self.isPlaying = bool(1-self.isPlaying)
                    # 键盘按下a
                    elif 97 == key:
                        self.isPlaying = False
                        self.cap.set(cv2.CAP_PROP_POS_FRAMES, trackPos-1)
                        ret, img = self.cap.read()
                        self.cap.set(cv2.CAP_PROP_POS_FRAMES, trackPos - 1)
                        cv2.setTrackbarPos("frames:", self.windowName, trackPos-1)
                        # cv2.imshow(self.windowName, img)
                        self.process_img(img)
                    elif 100 == key:
                        self.isPlaying = False
                        self.cap.set(cv2.CAP_PROP_POS_FRAMES, trackPos + 1)
                        ret, img = self.cap.read()
                        self.cap.set(cv2.CAP_PROP_POS_FRAMES, trackPos + 1)
                        cv2.setTrackbarPos("frames:", self.windowName, trackPos + 1)
                        # cv2.imshow(self.windowName, img)
                        self.process_img(img)
                    print(KEY_ENUM[key])
        print("退出处理函数！")

# 在此处定义处理函数
# 处理函数1；不做任何处理原图播放
def process1(img):
    return img

def process2(img):

    pass

if __name__ == '__main__':
    VideoPath = "/media/cobot/doc/data/5/5.mp4"
    cap = Capture( VideoPath)
    cap.set_process_func(process1)
    cap.startProcessing()

    print("退出程序")

