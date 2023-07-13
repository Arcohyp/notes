# 更换cuda版本
https://blog.csdn.net/xiaojinger_123/article/details/121158255

cd /usr/local/cuda-11.6/bin/
sudo ./cuda-uninstaller
sudo rm -rf /usr/local/cuda-11.6
sudo rm -rf /usr/local/cuda
sudo rm -rf /usr/local/cuda-11

# 以上是常规方法，如果找不到卸载文件，只能暴力删除
dpkg -l | grep cuda
# 查看所有cuda开头的，注意版本号，不要把驱动和cudnn删除了
sudo dpkg -P <filename>
# 如果有关联包裹，层层删除，非常麻烦
# 清除所有rc的包裹
dpkg -l | grep ^rc | cut -d' ' -f3 | sudo xargs dpkg --purge


# 更换cudnn
sudo dpkg -l | grep cudnn
# 同上面

# github登陆
# 1029282198@qq.com
# 最老的那个密码

# 永久的
sudo gedit ~/.bashrc
# 文件里添加这个
export PATH=/usr/local/cuda-11.1/bin:$PATH
export LD_LIBRARY_PATH=/usr/local/cuda-11.1/lib64:$LD_LIBRARY_PATH
      
