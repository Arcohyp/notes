https://blog.csdn.net/qq_33419535/article/details/88547498

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
