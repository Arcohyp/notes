## 遇到的ping不成功的问题

可能被重置为了192.168.1.111，直接ping这个就行，不要ping机器上面的ip

如果以上都不是，并且有时间的话，可以考虑把这个网段内的所有ip都ping一下
https://blog.csdn.net/qq_42197548/article/details/106669863

for /L %d in (1,1,255) do ping 192.168.0.%d >> C:\Users\XXX\Desktop\a.txt
