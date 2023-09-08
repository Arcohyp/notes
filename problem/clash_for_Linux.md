# Clash for Linux

> **[下载和简单使用]** : https://blog.iswiftai.com/posts/clash-linux/
>
> **[搭建订阅转服务前后端]** : https://blog.iswiftai.com/posts/docker-subscription-converter/

- 后端：127.0.0.1:25500
- 前端：127.0.0.1:58080

直接访问前端，粘贴url，之后可以直接访问转换后的url，复制并保存对应的yaml文件，粘贴到/home/.../.config/clash里的config.yaml文件当中

运行./clash
export https_proxy=http://127.0.0.1:7890 http_proxy=http://127.0.0.1:7890 all_proxy=socks5://127.0.0.1:7890


## 访问huggingface出现301 
https://blog.csdn.net/taipoucha5799/article/details/109490041
