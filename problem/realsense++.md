# 零、基础案例
https://github.com/IntelRealSense/librealsense/tree/master/wrappers/python/examples

最主要的是案例2和案例3，一个是对实时图片的读取，另一个是利用实时图片和深度图，排除出背景（比如yolo的用法）

# 一、+ yolov5案例(2023.8.25)
https://github.com/Thinkin99/yolov5_d435i_detection

https://blog.csdn.net/Thinkin9/article/details/122913810

## 1.环境配置过程
本人使用ubuntu 20.04 + cpu的方式进行测试

### （1）pip install -r requirements的末尾报错
(以下报错在没有创建新的虚拟环境的情况下，如果没有明确指定python版本也会出现该情况，即出现conda-meta而找不到bin等其他的安装包。如果执行以上的安装命令，实质是在base的基础上安装这些包)

> ERROR: pip's dependency resolver does not currently take into account all the packages that are installed. This behaviour is the source of the following dependency conflicts.
> 
> google-cloud-storage 1.31.0 requires google-auth<2.0dev,>=1.11.0, but you have google-auth 2.22.0 which is incompatible.
> 
> google-cloud-core 1.7.1 requires google-auth<2.0dev,>=1.24.0, but you have google-auth 2.22.0 which is incompatible.
> 
> google-api-core 1.25.1 requires google-auth<2.0dev,>=1.21.1, but you have google-auth 2.22.0 which is incompatible.

- **解决方法**
  
安装这两个版本google-auth==1.35.0 google-auth-oauthlib==0.5.3

### （2）python rstest.py报错
设备连接不好就重连

#### <1> opencv 与 numpy 纠葛
> TypeError: 'numpy._DTypeMeta' object is not subscriptable

查看版本，问题主要在于opencv-python更新动作大扯到了numpy
> opencv-python                 4.8.0.76
> 
> numpy                         1.21.5

- **解决方法**

安装这个版本opencv-python 4.7.0.68

### <2> upsample报错没有recompute_scalse_factor
> AttributeError: 'Upsample' object has no attribute 'recompute_scale_factor'

https://blog.csdn.net/qq_40280673/article/details/125095353

- **解决方法**

直接修改上面的文件即可
