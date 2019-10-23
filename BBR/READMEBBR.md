## **搭建过程中如果遇到任何问题，可联系我协助解决，QQ：2995350293**

**BBR是谷歌出品的TCP拥塞控制算法，有人专门测试过，安装后网速会提升数倍，魔改版的BBR甚至能到几十倍(这个感觉有点夸张了)**

### 原版BBR安装

1.获取脚本并自动执行脚本
```
wget --no-check-certificate https://github.com/teddysun/across/raw/master/bbr.sh && chmod +x bbr.sh && ./bbr.sh
```
2.安装完成后如果有提示重启，则输入y进行重启 

3.重启成功后，重新连接服务器,输入如下命令进行验证是否安装成功：  
```
sysctl net.ipv4.tcp_congestion_control
```
如果出现如下结果则表示安装成功：  
net.ipv4.tcp_congestion_control = bbr   

### 魔改版BBR安装（这里选择比较流行的南琴浪版）
1.获取脚本并自动执行脚本  
Debian版：
```
wget --no-check-certificate https://github.com/tcp-nanqinlang/general/releases/download/3.4.2.1/tcp_nanqinlang-fool-1.3.0.sh
bash tcp_nanqinlang-fool-1.3.0.sh
```
CentOS版：
```
wget --no-check-certificate https://raw.githubusercontent.com/tcp-nanqinlang/general/master/General/CentOS/bash/tcp_nanqinlang-1.3.2.sh
bash tcp_nanqinlang-1.3.2.sh
```
2.出现下图提示时，输入数字1选择安装内核，然后回车：  

<img src="https://github.com/smallqiangno/use-guide/blob/master/BBR/bbr1.jpg" width="271" height="107" alt="图片加载失败时，显示这段字"/>  
3.接下来的安装过程中，部分系统可能会有如下提示，提示删除旧的内核，是否取消。这是选择No后回车，确认删除。

<img src="https://github.com/smallqiangno/use-guide/blob/master/BBR/bbr2.jpg" width="600" height="290" alt="图片加载失败时，显示这段字"/>  
4.安装内核成功后会出现如下提示，输入reboot回车重启系统：  

<img src="https://github.com/smallqiangno/use-guide/blob/master/BBR/bbr3.jpg" width="559" height="117" alt="图片加载失败时，显示这段字"/>  
5.重启后，找到开始脚本下载的目录，输入如下命令：  
```
bash tcp_nanqinlang-1.3.2.sh
```  

出现如下界面，输入2安装并开启算法：  

<img src="https://github.com/smallqiangno/use-guide/blob/master/BBR/bbr4.jpg" width="271" height="107" alt="图片加载失败时，显示这段字"/>  
6.稍等片刻，安装成功后的提示如下图：   

<img src="https://github.com/smallqiangno/use-guide/blob/master/BBR/bbr5.jpg" width="367" height="69" alt="图片加载失败时，显示这段字"/>  

7.检查算法是否在运行，按照第五步的操作，输入3即可   







