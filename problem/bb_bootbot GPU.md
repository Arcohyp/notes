# Reporting errors of bb@nuc-bootbot

This issue is still opening, I DO NOT know how to sovle it. Now I just list the points that I have already known.

## Question: When using *rviz* or *rqt_tf_tree*, for example, terminal will show the errors as below:
    rviz
![image](https://github.com/Arcohyp/notes/blob/main/problem/pic/Screenshot%20from%202023-08-31%2008-57-21.png)

Here are three main clues, or keywords:

> screen 0 does not appear to be DRI2 capable
>
> screen 0 does not appear to be DRI2 capable
> 
> amdgpu_device_initialize: amdgpu_get_auth (1) failed (-1)
>
> Segmentation fault

- GPU is ***[AMD/ATI] Polaris 22 [Radeon RX Vega M GL]***. 

- CPU is ***i7-8705G CPU @ 3.10GHz*** and architecture is ***x86_64***.

- GPU is independent, but it binds to with CPU because CPU has a letter of ‘G’.


    lspci -vnn | grep VGA
![image](https://github.com/Arcohyp/notes/blob/main/problem/pic/Screenshot%20from%202023-08-31%2008-59-09.png)

    lscpu
![image](https://github.com/Arcohyp/notes/blob/main/problem/pic/Screenshot%20from%202023-08-31%2008-59-33.png)

    sudo lshw -C video
![image](https://github.com/Arcohyp/notes/blob/main/problem/pic/Screenshot%20from%202023-08-31%2009-14-11.png)

