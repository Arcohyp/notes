# 使用 Realsense2 相机遇到的各种问题
## 一、安装过程中遇到的报错
https://blog.csdn.net/qq_33419535/article/details/88547498

https://www.jianshu.com/p/fb5920af58aa

https://blog.csdn.net/wanghq2013/article/details/123325671

官方文档：https://github.com/IntelRealSense/librealsense/blob/master/doc/installation.md

### 更新系统的时候会出现的问题 
    sudo upgrade-grub
    sudo reboot

开不了机，end kernel panic not syncing报错

https://blog.csdn.net/avatar_2009/article/details/116233098

系统启动时进ubuntu的高级选项设，选择旧的核心版本启动，成功进入系统。启动系统,在启动过程中,反复按shift键 (通过上下键移动,选择 Ubuntu 选项 (或者有的版本显示的是Advanced options for Ubuntu),然后按’Enter’键, 进入正常登录界面

（据此继续升级，应该可以根本上解决问题）。我这里有三个，76，41，52，出问题的就是76

这才刚刚开始。

    uname -r
    dpkg --get-selections | grep linux

此时可以选择不升级（但这失去了意义）

    sudo apt-get remove linux-headers-xxxx

注意输入上面这段的时候，会发现nvida的部分包裹需要common-525的支持，此时

    sudo apt-get install (上面的这个需要支持的包裹)

重启电脑，就可以了

【已解决】打patch补丁时出错：Reversed (or previously applied) patch detected! Assume -R? [n]

hunks FAILED -- saving rejects to file

输入 n就行：https://blog.csdn.net/Q_AN1314/article/details/100521766

    sudo dmesg | tail -n 50

执行上面这个语句的时候，需要把摄像头接到电脑上面才行

执行sudo make uninstall && make clean && make && sudo make install 会出现逆天git clone，没办法，翻出去再尝试吧

## 二、hand_eye遇到的报错
https://blog.csdn.net/miss_future/article/details/111826016

rosdep 需要 ros环境

    pip install transforms3d
    pip install catkin_pkg
    pip install empy
    pip install pyyaml

【解决问题】RLException: [xx.launch] is neither a launch file in package [x] nor is [x] a launch file name

https://blog.csdn.net/weixin_44436677/article/details/106442240

## 三、SDK中的example使用
不太推荐使用g++进行编译，官方推荐使用的是CMake工具

    mkdir build && cd build && cmake .. && make

https://github.com/IntelRealSense/librealsense/issues/5651

但g++也不是不行，比如想要跑这个代码：https://github.com/IntelRealSense/librealsense/tree/master/examples/hello-realsense#rs-hello-realsense-sample
    
    g++ rs-hello-world.cpp -o test -lrealsense2

## 四、打开realsense-viewer弹出udev-rules报错，并且无法显示rgb和实时相机画面
具体的报错信息如下：

> Timestamp: 1692926219631.358154
> Severity: Warn
> Description: Multiple realsense udev-rules were found! :
> 1:/etc/udev/rules.d/99-realsense-libusb.rules
> 2: /lib/udev/rules.d/60-librealsense2-udev-rules.rules
> Make sure to remove redundancies!

我之前安装了librealsense2-dkms这个库，其实不必要的，使用以下语句删除：

    sudo apt-get autoremove librealsense2-dkms

删除过后，再删去以上提到的两个文件：

    sudo rm /etc/udev/rules.d/99-realsense-libusb.rules
    sudo rm /lib/udev/rules.d/60-librealsense2-udev-rules.rules

此时打开realsense-viewer，会报出缺失错误：

> Timestamp: 1692927374126.788086
> Severity: Warn
> Description: RealSense UDEV-Rules are missing!
> UDEV-Rules permissions configuration 
> for RealSense devices.

点开有2个选项，copy command之后粘贴可以发现以下信息：

> Missing/outdated UDEV-Rules will cause 'Permissions Denied' errors
> unless the application is running under 'sudo' (not recommended)
> In case of Debians use: 
> sudo apt-get upgrade/install librealsense2-udev-rules
> To manually install UDEV-Rules in terminal run:
> $ sudo cp ~/.99-realsense-libusb.rules /etc/udev/rules.d/99-realsense-libusb.rules && sudo udevadm control --reload-rules && udevadm trigger

直接使用最后一句解决问题：

    sudo cp ~/.99-realsense-libusb.rules /etc/udev/rules.d/99-realsense-libusb.rules && sudo udevadm control --reload-rules && udevadm trigger
    
