### ROS报错：-- Could NOT find PY_em (missing: PY_EM)
https://blog.csdn.net/tanmx219/article/details/122765853

替换catkin为这个
catkin_make -DPYTHON_EXECUTABLE=/usr/bin/python3

### 创建ROS工作空间的时候的几个位置填什么
echo $ROS_PACKAGE_PATH /home/<username>/catkin_ws/src:/opt/ros/<distro>/share

这个distro其实是版本，你可以在桌面开terminal，cd /，ls，就能看到opt文件了，进入找就可以

echo $ROS_PACKAGE_PATH /home/ros/catkin_ws/src:/opt/ros/noetic/share


