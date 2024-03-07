## 在终端terminal使用代理，当次有效
### https
    export https_proxy=https://127.0.0.1:7890
### http
    export http_proxy=http://127.0.0.1:7890

### gntuls_handshake() failed: The TLS connection was non-properly terminated.
    git config --global http.https://github.com.proxy http://127.0.0.1:7890
    git config --global https.https://github.com.proxy https://127.0.0.1:7890

### RPC failed; curl 56
    git config --global http.postBuffer 1048576000
    # 1G buffer size
