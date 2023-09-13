# bb_new 复刻原版bb代码运行环境
## 0.基本安装
- 系统：Ubuntu 18.04 LTS
- 基本软件：steam++，vscode，baiduwangpan，sogoupinyin

- vim，net-tools,etc 前4命令 
> https://blog.csdn.net/yzf279533105/article/details/105101275

- 一键安装ros，rosdep
> https://fishros.org.cn/forum/topic/20/%E5%B0%8F%E9%B1%BC%E7%9A%84%E4%B8%80%E9%94%AE%E5%AE%89%E8%A3%85%E7%B3%BB%E5%88%97?lang=en-US

- visp、visp_ros、vision_visp,前3命令
> https://blog.csdn.net/qq_36104364/article/details/113192324

## 1.catkin_make 原版，安装所有依赖包
先删去build，直接catkin_make

### 已经安装sophus

### 已经安装这个ros-melodic-navigation
	sudo apt-get install ros-melodic-navigation

### No package 'orocos-bfl' found
	sudo apt-get install ros-melodic-bfl

### Unable to find SuiteSparse
	sudo apt-get install libsuitesparse-dev

### Could not find libg2o!
	sudo apt-get install ros-melodic-libg2o

### ros编译出现moveit_visual_toolsConfig.cmake
	sudo apt-get install ros-melodic-moveit-visual-tools

### Could not find a package configuration file provided by "realsense2_camera"
	sudo apt-get install ros-melodic-realsense2-camera

#### 不知道下面有用与否，也安装了
安装realsense支持，参考另一篇

##### git 不了 libcurl 
> https://blog.csdn.net/u012742444/article/details/120067772?spm=1001.2101.3001.6650.2&utm_medium=distribute.pc_relevant.none-task-blog-2%7Edefault%7ECTRLIST%7ERate-2-120067772-blog-124400633.235%5Ev38%5Epc_relevant_sort&depth_1-utm_source=distribute.pc_relevant.none-task-blog-2%7Edefault%7ECTRLIST%7ERate-2-120067772-blog-124400633.235%5Ev38%5Epc_relevant_sort&utm_relevant_index=3

- ***realsense-viewer***可呼出

### fatal error: pcap.h: No such file or directory
	sudo apt-get install libpcap-dev

### fatal error: xarm/wrapper/xarm_api.h: No such file or directory
安装xarm c plus sdk

- ***catkin_make通过***

## 2.尝试launch
	source ~/Desktop/catkin_ws/devel/setup.bash
	roslaunch ~/Desktop/catkin_ws/src/arm/xarm_ros/xarm_planner/launch/xarm_planner_pick_place_real.launch

### 报错The kinematics plugin (xarm_f) failed to load. Error: According to the loaded plugin descriptions the class trac_ik_kinematics_plugin/TRAC_IKKinematicsPlugin with base class type kinematics::KinematicsBase does not exist. Declared types are  cached_ik_kinematics_plugin/CachedKDLKinematicsPlugin cached_ik_kinematics_plugin/CachedSrvKinematicsPlugin kdl_kinematics_plugin/KDLKinematicsPlugin lma_kinematics_plugin/LMAKinematicsPlugin srv_kinematics_plugin/SrvKinematicsPlugin

	sudo apt-get install ros-melodic-trac-ik-kinematics-plugin

### 报错
Traceback (most recent call last):
  File "/home/bb_new/Desktop/catkin_ws/src/arm/easy_handeye/easy_handeye/scripts/publish.py", line 15, in <module>
    calib.from_file()
  File "/home/bb_new/Desktop/catkin_ws/src/arm/easy_handeye/easy_handeye/src/easy_handeye/handeye_calibration.py", line 163, in from_file
    with open(self.filename) as calib_file:
IOError: [Errno 2] No such file or directory: '/home/bb_new/.ros/easy_handeye/xarm_b_real_calib_result_eye_on_hand.yaml'
Traceback (most recent call last):
  File "/home/bb_new/Desktop/catkin_ws/src/arm/easy_handeye/easy_handeye/scripts/publish.py", line 15, in <module>
    calib.from_file()
  File "/home/bb_new/Desktop/catkin_ws/src/arm/easy_handeye/easy_handeye/src/easy_handeye/handeye_calibration.py", line 163, in from_file
    with open(self.filename) as calib_file:
IOError: [Errno 2] No such file or directory: '/home/bb_new/.ros/easy_handeye/xarm_f_real_calib_result_eye_on_hand.yaml'

两个错误其实一样的，没文件、或者文件存在但地址索引不正确

	cp -r ~/Desktop/catkin_ws/src/arm/easy_handeye/calibrate_result/result/. ~/.ros/easy_handeye/

### launch 
将

	source ~/Desktop/catkin_ws/devel/setup.bash
加入到~/.bashrc最后，并立即

	source ~/.bashrc

可以直接执行
	
	roslaunch xarm_planner xarm_planner_pick_place_real.launch

***【2023年9月6日】***

**！！！注意！！！**

当前bb_new已经出现不同版本分支，原版本以镜像形式存储在外接硬盘当中

| 不同版本分支 | 所处主机、位置|
| ------ | ------ |
| ***bb_new原版镜像*** | 外接硬盘|
| ***版本1*** | 架子上的主机 | 
| ***版本2*** | nuc11PHi7C | 

# 以上环境配置结束

## 3.bb_new覆盖新的nuc
intel nuc使用***F2***进入bios界面，当然也可以直接使用***F10***进行选择启动引导

### 使用再生龙方式覆盖
> https://github.com/Arcohyp/notes/blob/main/problem/%E5%86%8D%E7%94%9F%E9%BE%99%E5%A4%87%E4%BB%BD%E7%B3%BB%E7%BB%9F.md#%E4%BD%BF%E7%94%A8%E5%86%8D%E7%94%9F%E9%BE%99%E5%A4%87%E4%BB%BDubuntu%E7%B3%BB%E7%BB%9F%E7%9B%98

### 覆盖后开机花屏解决方式
> https://zhuanlan.zhihu.com/p/439088148
>
> https://askubuntu.com/questions/1024895/why-do-i-need-to-replace-quiet-splash-with-nomodeset

- GPU版本：GeForce RTX 2060 Mobile（notebook）
- CPU版本：i7-1165G7

# 以上迁移结束

## 4. 安装显卡驱动
> https://www.nvidia.cn/geforce/drivers/
> 
> https://zhuanlan.zhihu.com/p/463656273

## 5. 修改模型尺寸
> xarm6.urdf.xacro
> 
>> 修改的是xarm底部的红色方块和碰撞检测区域（和底盘）
>
> xarm6_robot.urdf.xacro
>
>> 修改的是xarm的位置

参考坐标系是世界坐标系，具体与小车如何绑定，*应该*在其他文件当中

## 6. 仿真
## 1) 执行底盘的话问题比较多，很多没解决
### [Err] [REST.cc:205] Error in REST request
> https://blog.csdn.net/qq_43802597/article/details/97996255

### Spawn service failed
> https://blog.csdn.net/qq_40113966/article/details/120442227

### ERROR: cannot launch node of type [yocs_virtual_sensor/yocs_virtual_sensor_node]: Cannot locate node of type [yocs_virtual_sensor_node] in package [yocs_virtual_sensor]. Make sure file exists in package path and permission is set to executable (chmod +x)

### ImportError: No module named rospy_message_converter
	sudo apt install python-pip
 	pip install rospy-message-converter

这个玩意装过了


### IOError: Path "." is neither a directory containing a "package.xml" file nor a file

## 2) 执行 pick and place 
### 找不到 *pose_base_controller/pose_base_controller_gazebo* 
> https://github.com/ros-planning/navigation_experimental/tree/melodic-devel
下载上面的，放到src里面

	catkin_make
 	source devel/setup.bash

pose_base_controller_gazebo.launch文件修改type
>   <node type="pose_base_controller" pkg="pose_base_controller" name="pose_base_controller" output="screen">

### Could not find a package configuration file provided by "SBPL" with any of   the following names: 
	sudo apt-get install ros-melodic-sbpl

### [gazebo-2] process has died [pid 7920, exit code 255.....“的问题

使用Ctrl+C结束当前运行，然后输入

	killall gzserver

直接关掉也行，但还是需要source

## 以上
