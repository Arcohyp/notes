### 遇到的ping不成功的问题

可能被重置为了192.168.1.111，直接ping这个就行，不要ping机器上面的ip

如果以上都不是，并且有时间的话，可以考虑把这个网段内的所有ip都ping一下
https://blog.csdn.net/qq_42197548/article/details/106669863

其中xxx是你的用户名

for /L %d in (1,1,255) do ping 192.168.1.%d >> C:\Users\XXX\Desktop\a.txt

for /L %D in (1,1,255) do (ping 192.168.1.%D -n 1 && echo 192.168.1.%D >> C:\Users\XXX\Desktop\a.txt || echo 192.168.1.%D >> C:\Users\XXX\Desktop\b.txt)

当前，206和220都已经被设置为正确的ip地址，207使用上述脚本并未能找到对应的ip地址

### 其他关于ping的问题
按照xarm 用户手册 60/191的内容，可以选择双机械臂连接同一个路由器，主机（服务器）连接这个路由器构建的局域网的方式连接这2个机械臂并获得控制权。

可能会遇到的其他问题：

#### 1.如果重置了/或是没重置路由器，是无法直接从主机ping到它们的
这个时候按照设备上的信息重置，TP-LINK_854b的后台是***192.168.1.1***


### 安装依赖
http://wiki.ros.org/xarm
记得换成noetic

两个依赖包都在站内找，搜索xarm的前两个，下下来解压

官方教程里面的有个安装包是这个链接：https://github.com/roboticsgroup/roboticsgroup_gazebo_plugins
教程：https://github.com/mintar/mimic_joint_gazebo_tutorial

launch文件中param、rosparam以及arg之间的区别: https://blog.csdn.net/weixin_45777375/article/details/109445591


