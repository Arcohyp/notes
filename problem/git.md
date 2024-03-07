## Using Agent Proxy in terminal by once
### https
    export https_proxy=https://127.0.0.1:7890
### http
    export http_proxy=http://127.0.0.1:7890

## git from github
STRONGLY RECOMMEND using git to download project. If you want to static use open-source code, you can download it. But if the project need to be synchronized, you MUST use git.

### gntuls_handshake() failed: The TLS connection was non-properly terminated.
    git config --global http.https://github.com.proxy http://127.0.0.1:7890
    git config --global https.https://github.com.proxy https://127.0.0.1:7890

### RPC failed; curl 56
    git config --global http.postBuffer 1048576000
    # 1G buffer size

### podman
Just like Docker. Using Dockfile to create image, using image to create container.
- Dockfile: like a json file to create an image.
- image: like a exe file, but not allocate any memory or cpu.
- container: like a progress.

        # list
        podman images
        podman cotainer list -a
        # Delete
        podman stop [containr_id]
        podman start [container_name] -a
        podman rm [containr_id/name]
        podman rmi [image_id/name]
        
        podman-compose up # In conda virtual environment

### docker-compose.yaml
      https://zhuanlan.zhihu.com/p/387840381
