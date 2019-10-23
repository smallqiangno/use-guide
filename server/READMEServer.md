## **搭建过程中如果遇到任何问题，可联系我协助解决，QQ：2995350293**

## 第一步：如何购买一台VPS

对于具有选择困难症的人来说，选择哪家运营商确实是件头疼的事情，首先定个大基调，一分价钱一分货。由于个人需要，我用过不少运营商的VPS，这里就把我的体验给各位猿友们分享一下！

[购买VPS教程](https://github.com/smallqiangno/use-guide/blob/master/server/READMEBuyVps.md)
 
## 第二步：安装SSR：

我们使用的是逗比的一键安装脚本，非常省事而且功能强大,适合自己搭建梯子建若干个账户来用，如果账户很多，那就需要面板的方法了，面板的方法在下一篇文章中讲解！其特点如下：

* 支持 限制 用户速度
* 支持 限制 端口设备数
* 支持 显示 当前连接IP
* 支持 显示 SS/SSR连接+二维码
* 支持 切换管理 单/多端口
* 支持 一键安装 锐速（VPS必须是KVM架构）
* 支持 一键安装 BBR（VPS必须是KVM架构）
* 支持 一键封禁 垃圾邮件(SMAP)/BT/PT

### 第一步：获取逗比脚本
```$xslt
wget -N --no-check-certificate https://raw.githubusercontent.com/ToyoDAdoubi/doubi/master/ssr.sh && chmod +x ssr.sh && bash ssr.sh
```
注意：
* 第14项，是指与SSR无关的其它功能，比如锐速/BBR安装等。本文随后专门介绍。
* 关于第3项的libsodium：如果你在随后安装中，准备选择的加密方式是chacha20系列，那么需要额外安装这个，其它加密方式可以忽略。另外目前逗比的脚本中虽然提供了安装libsodium的选项，但是其是不可用的，如果需要我们需另外安装它，稍后会介绍如何单独安装libsodium！
* 下面的示例中我设置的参数和脚本推荐的参数不一致，这个可以根据自己需要进行设置!
* 逗比的脚本中不提供混淆参数和协议参数的配置，原因是其认为这些参数无利于防封而且会降低5%到10%左右的速度，但我见过的小型商业化的系统其是配置这两个参数的！

<img src="https://github.com/smallqiangno/use-guide/blob/master/server/server1.png" width="833" height="398" alt="图片加载失败时，显示这段字"/>  

### 第二步：输入数字1，开始安装，首先要先设置端口
<img src="https://github.com/smallqiangno/use-guide/blob/master/server/server2.png" width="796" height="84" alt="图片加载失败时，显示这段字"/>  

### 第三步：设置密码
<img src="https://github.com/smallqiangno/use-guide/blob/master/server/server3.png" width="852" height="110" alt="图片加载失败时，显示这段字"/>  
   
### 第四步：设置加密算法，这里设置none
<img src="https://github.com/smallqiangno/use-guide/blob/master/server/server4.png" width="798" height="444" alt="图片加载失败时，显示这段字"/>  

### 第五步：设置协议，这里设置auth_chain_a
<img src="https://github.com/smallqiangno/use-guide/blob/master/server/server5.png" width="717" height="188" alt="图片加载失败时，显示这段字"/>  

### 第六步：设置混淆，这里设置tls1.2_ticket_auth
<img src="https://github.com/smallqiangno/use-guide/blob/master/server/server6.png" width="811" height="204" alt="图片加载失败时，显示这段字"/>  

提示是否兼容原版，这里选择不兼容：n
<img src="https://github.com/smallqiangno/use-guide/blob/master/server/server7.png" width="766" height="85" alt="图片加载失败时，显示这段字"/>  

### 第七步：设置设备数限制、网速限制（这里我没设置，因为自己使用，你还限制个锤子）
<img src="https://github.com/smallqiangno/use-guide/blob/master/server/server8.png" width="825" height="202" alt="图片加载失败时，显示这段字"/>  

### 第八步：以上设置完成后，就进入了安装过程，如果需要输入y的时候输入y即可，耐心等待，最后成功的结果如图所示，拷贝ssr链接到客户端即可
<img src="https://github.com/smallqiangno/use-guide/blob/master/server/server9.png" width="889" height="385" alt="图片加载失败时，显示这段字"/>  


### 额外步骤1：如果加密方式是chacha20系列，则需要安装libsodium，安装方式如下：
1. 下载最新稳定版本
wget -N --no-check-certificate https://github.com/jedisct1/libsodium/releases/download/1.0.18-RELEASE/libsodium-1.0.18.tar.gz
2. 解压
tar xf libsodium-1.0.18.tar.gz && cd libsodium-1.0.18
3. 编译
./configure --disable-maintainer-mode && make -j2 && make install
4. 配置
echo /usr/local/lib > /etc/ld.so.conf.d/usr_local_lib.conf
ldconfig  

### 额外步骤2：安装BBR加速工具,BBR是谷歌出品的TCP拥塞控制算法，有人专门测试过，安装后网速会提升数倍，魔改版的BBR甚至能到几十倍(这个感觉有的夸张了)
#### 原版BBR安装
1. 获取脚本并自动执行脚本
```wget --no-check-certificate https://github.com/teddysun/across/raw/master/bbr.sh && chmod +x bbr.sh && ./bbr.sh
```
2.安装完成后如果有提示重启，则输入y进行重启  
3.重启成功后，重新连接服务器,输入如下命令进行验证是否安装成功：  
```
sysctl net.ipv4.tcp_congestion_control
```
如果出现如下结果则表示安装成功：
net.ipv4.tcp_congestion_control = bbr

