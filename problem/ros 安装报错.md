### 1.ROS报错：-- Could NOT find PY_em (missing: PY_EM)
https://blog.csdn.net/tanmx219/article/details/122765853

替换catkin为这个

    catkin_make -DPYTHON_EXECUTABLE=/usr/bin/python3

### 2.创建ROS工作空间的时候的几个位置填什么
    echo $ROS_PACKAGE_PATH /home/<username>/catkin_ws/src:/opt/ros/<distro>/share

这个distro其实是版本，你可以在桌面开terminal，cd /，ls，就能看到opt文件了，进入找就可以

    echo $ROS_PACKAGE_PATH /home/ros/catkin_ws/src:/opt/ros/noetic/share

### 3.ROS报错:sudo rosdep init website
直接参考下面这个链接就行：

博客解决方案：https://blog.csdn.net/weixin_42335881/article/details/119728301?spm=1001.2101.3001.6650.1&utm_medium=distribute.pc_relevant.none-task-blog-2%7Edefault%7ECTRLIST%7ERate-1-119728301-blog-120590026.235%5Ev38%5Epc_relevant_sort_base3&depth_1-utm_source=distribute.pc_relevant.none-task-blog-2%7Edefault%7ECTRLIST%7ERate-1-119728301-blog-120590026.235%5Ev38%5Epc_relevant_sort_base3&utm_relevant_index=2

http://www.autolabor.com.cn/book/ROSTutorials/chapter1/12-roskai-fa-gong-ju-an-zhuang/124-an-zhuang-ros.html

视频解决方案：https://www.bilibili.com/video/BV1Ci4y1L7ZZ?p=16&vd_source=bbca381483664de7941cac6af725c6df

国内源：https://gitee.com/zhao-xuzuo/rosdistro

### 4.ROS:ModuleNotFoundError: No module named ‘rospkg‘
采用方法1：https://blog.csdn.net/qq_42995327/article/details/119357775

    pip install catkin-tools rospkg pyyaml empy numpy

如果不想污染base环境，可以重新构建一个ros环境

    conda create -n ros
    conda activate ros
    pip install catkin-tools rospkg pyyaml empy numpy

此时还会报错少pydot，安装就行

    pip install pydot

### 执行C++ Helloworld
分清，workspace,包名，和代码cpp的文件名很重要

    -*workspace（比如catkin_ws）
    --build
    --devel
    --src
    ---*你的包名(比如demo,etc)
    ----include
    ----src
    -----*文件名（比如helloworld,etc）.cpp
    ----*CMakeLists.txt（你要修改的是这个文件，很多注释的）
    ----package.xml
    ---CMakeLists.txt
