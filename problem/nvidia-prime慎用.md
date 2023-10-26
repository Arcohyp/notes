## 使用这个命令会出现gpu调用不了的情况，无论怎样重新安装都会发现nvidia-drm被禁用

    sudo prime-select intel
    sudo prime-select nvidia

https://blog.csdn.net/tianlangstudio/article/details/115278135

如果使用prime-select intel，就会在modprobe处强制编写conf文件使得nvidia相关的的内核被禁用，此时强制删除后，再重启，再一次安装nvidia驱动
