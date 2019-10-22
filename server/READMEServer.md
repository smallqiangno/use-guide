## **搭建过程中如果遇到任何问题，可联系我协助解决，QQ：2995350293**

## 第一步：如何购买一台VPS

对于具有选择困难症的人来说，选择哪家运营商确实是件头疼的事情，首先定个大基调，一分价钱一分货。由于个人需要，我用过不少运营商的VPS，这里就把我的体验给各位猿友们分享一下！

1.【**Vultr**】
 [官网](https://my.vultr.com/)
 
 优点：全球节点众多、机房新、按小时收费、控制台非常友好，免费更换IP.....  
 
 缺点：由于现在Vultr升级后太过受欢迎，导致使用者甚多，所以其日本、新加坡、美国三个地方分配的IP大概率都是被墙了的，略无奈......
 
 **推荐指数:★★★★★**

2.【**搬瓦工**】
[官网](https://bandwagonhost.com/)

优点：老牌运营商，之前是小白入门之选，但现在搬瓦工开始走中高端路线了(走高端路线能不能先升级下官网)，其它我就不知道了......  

缺点：官网太丑，官网太丑，官网太丑......

**推荐指数:★★★**

3.【**Kdatacenter**】
[官网](https://www.kdatacenter.com)

优点：韩国原生IP，延迟很低，速度快，可用来打游戏，VPS性能非常的好也非常的稳定  
缺点：只卖韩国的VPS、价格略高、流量给的也少，人家这么设置价格可能就是想把众多小白拒之门外！

**推荐指数:★★★★**

4.【**DMIT**】
[官网](https://www.dmit.io)

优点：香港VPS首选，速度最快、最稳定，但经常断货；美国主机也相当不错，这是我见过的唯一一家登陆服务器只能通过私钥登陆，不能通过用户名和密码的运营商，这非常酷！  

缺点：香港VPS很难买到，价格也偏贵，但我还是那句话，一分价钱一分货！

**推荐指数:★★★★★**

5【**Raksmart**】
[官网](https://www.raksmart.com)

海外华人创办的公司，当时买香港的专机时了解到的这家运营商，买了一台使用了一下，中规中矩，没有什么特殊优势和劣势！

**推荐指数:★★★**


6.【**DigitalOcean**】
[官网](https://cloud.digitalocean.com)

这个我没使用过，因为注册后，它说我恶意注册，锁了我的账户，发了邮件后才给我解除，但后来我也不想用它家的产品了！不过这家也是不错的运营商！

**推荐指数:★★★**

7.【**Linode**】
[官网](https://www.linode.com)

这个也是注册后，识别我恶意注册，可能是当时我用的代理连的网注册的，后来索性不用！不过也是家还不错的运营商！

**推荐指数:★★★★**


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


