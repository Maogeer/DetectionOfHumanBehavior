# iDT算法
iDT算法是行为识别领域中非常经典的一种算法，在深度学习应用于该领域前也是效果最好的算法。

+ 参考：
    +  [csdn行为识别笔记](https://blog.csdn.net/wzmsltw/article/details/53023363)
    +  [iDT算法用法与代码解析](https://blog.csdn.net/wzmsltw/article/details/53221179)
    +  [代码解析2](https://blog.csdn.net/zackzhaoyang/article/details/50881114)
+  **Key Word**:
    +  **HOG特征** 
        > 方向梯度直方图（Histogram of Oriented Gradient, HOG）,属于spatial（空间）特征

    +  **HOF特征**
        > HOF(Histogramsof Oriented Optical Flow)与HOG类似，是对光流方向进行加权统计，得到光流方向信息直方图。通常用于动作识别中；属于temporal（时间）的特征。
    +  **MBH特征**
        > 对于MBH特征，它的处理方法是将x方向和y方向上的光流图像视作两张灰度图像，然后提取这些灰度图像的梯度直方图。即MBH特征是分别在图像的x和y方向光流图像上计算HOG特征；属于temporal（时间）的特征。
    + **Dense Trajectory**
        > 某个特征点在连续的L帧图像上的位置即构成了一段轨迹$(p_t,p_{t+1},p_{t+2},\ldots,p_{t+L})$,后续的特征提取即沿着各个轨迹进行。由于特征点的跟踪存在漂移现象，故长时间的跟踪是不可靠的，所以每L帧要重新密集采样一次特征点，重新进行跟踪。在DT/iDT算法中，选取L=15。轨迹特征为15*2=30维向量。

    + **运动/结构描述子(HOF,HOG,MBH)**
    > + 几种特征提取的通用部分进行介绍。沿着某个特征点的长度为L的轨迹，在每帧图像上取特征点周围的大小为N×N的区域，则构成了一个时间-空间体（volume），如算法基本框架图的右半部分所示。对于这个时间-空间体，在进行一次网格划分，空间上每个方向上分为$n_\sigma $份，时间上则均匀选取$n_\tau $份。故在时间-空间体中共分出$n_\sigma\times n_\sigma\times n_\tau$份区域用作特征提取。在$DT/iDT$中，取$N=32,n_\sigma=2,n_\tau=3 $,接下来对各个特征的提取细节进行介绍。
    > + HOG特征:HOG特征计算的是灰度图像梯度的直方图。直方图的bin数目取为8。故HOG特征的长度为96（$2*2*3*8$）。
    > + HOF特征:HOF计算的是光流（包括方向和幅度信息）的直方图。直方图的bin数目取为8+1，前8个bin于HOG相同，额外的一个bin用于统计光流幅度小于某个阈值的像素。故HOF的特征长度为108（$2*2*3*9$）。
    > + MBH特征:MBH计算的是光流图像梯度的直方图，也可以理解为在光流图像上计算的HOG特征。由于光流图像包括x方向和y方向，故分别计算MBHx和MBHy。MBH总的特征长度为192（$2*96$）。
    > + 在计算完后，还需要进行特征的归一化，DT算法中对HOG,HOF和MBH均使用L2范数归一化。
    
    + **特征编码**
每段轨迹都对应着一组特征（trajectory,HOG,HOF,MBH），因此需要对这些特征组进行编码，得到一个定长的编码特征来进行最后的视频分类。
        + **DT**:使用[**Bag of Features**](https://blog.csdn.net/chlele0105/article/details/9633397)方法进行特征的编码。
        + **iDT**:使用[**Fisher Vector**](https://blog.csdn.net/wzmsltw/article/details/52040010)方法进行特征的编码


