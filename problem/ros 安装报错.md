### ROS报错：-- Could NOT find PY_em (missing: PY_EM)
https://blog.csdn.net/tanmx219/article/details/122765853

替换catkin为这个
catkin_make -DPYTHON_EXECUTABLE=/usr/bin/python3


echo $ROS_PACKAGE_PATH /home/<username>/catkin_ws/src:/opt/ros/<distro>/share

echo $ROS_PACKAGE_PATH /home/ros/catkin_ws/src:/opt/ros/noetic/share
