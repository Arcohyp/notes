# GL-iNET路由器相关问题
## 0.目前使用的的几款GL-iNET(我所知道的，待补充)
- GL-MT3000：一个lan，一个wan，wan可改成lan(2023.8.24未改)
  - SSID： Bootbot_WIFI/Bootbot_WIFI_5G
  - key: name of lab
  - ip: 192.168.8.1 
- GL-SFT1200：两个lan，一个wan，wan可改成lan(2023.8.28已改)

## 1.主要解决的是重置之后访问不了后台的问题
问题的本质：需要了解到GL-iNET路由器的内部有着OpenWRT的操作系统，这就使得它和普通的路由器有着不一样的操作

如果重启后直接连接，dhcp是不会分配ip的，系统会自动分配169开头的B类地址，这其实相当于没有分配，属于正常情况

使用uboot对路由器进行重启

- 文字版：
https://docs.gl-inet.cn/router/4/features/uboot/

- 注意：

版本是GL-MT3000，只需要下载uboot，也就是说下载的文件的后缀是**.img**

按住reset键后插入电源，闪6次蓝灯变白就行

等待三分钟就可以

- 视频版：
https://www.bilibili.com/video/BV1744y1x7rx/?spm_id_from=888.80997.embed_other.whitelist&t=1&vd_source=bbca381483664de7941cac6af725c6df
