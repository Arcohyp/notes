## 解决出现NET::ERR_CERT_AUTHORITY_INVALID的问题
下载的时候注意，下x86的那个，不要管amd64

点击启动的时候，首先不要信他弹出来的这个代理的问题，说你没开放403的端口，什么代理问题之类

说白了就是edge/或者说chrome内核的浏览器没有添加证书，具体内容参考这个连接

https://steampp.net/liunxSetupCer

  Steam 信任证书 ( Chrome 内核浏览器 )
  由于 Steam 使用 Chrome 内核浏览器，使用自管理证书库。
  需要使用 Chrome 打开 设置 - 隐私设置和安全性 - 安全 - 管理证书
  选择 授权机构( Authorities )
  在 Watt Toolkit 的设置 - 通用设置 - 存储空间 - 打开 AppData 目录中的
  SteamTools.Certificate.pem文件 导入
  注：如文件不存在可修改 SteamTools.Certificate.cer 为 SteamTools.Certificate.pem勾选 信任该证书，以标识网站身份

至于更多的可以参考这个连接

https://steampp.net/faq
