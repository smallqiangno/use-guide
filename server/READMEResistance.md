## **搭建过程中如果遇到任何问题，可联系我协助解决，QQ：2995350293**

## 如何避免自己搭建的节点较快的被封：
**曾经沧海难为水，对，就是那个曾经，what？ 曾经或者现在搭建自己节点的人肯定都有一个头疼的问题，那就是如何更好的规避GFW，以避免刚搭的梯子没过几天就折了，这里我根据搜集的资料和实操经验提供一些方法**

### 一. 合理的配置相关参数：
我的配置如下，这个也是我抄袭的之前卖给我梯子的那人的配置，我用了大概一年多，一直很稳定，有可能他的机器也被封过啊，只不过随时换了机器：
加密算法：none  
**协议：auth_chain_a  
混淆：tls1.2_ticket_auth  
混淆参数：pb.tedcdn.com（此处是伪装你正在访问此网站，很多人说没什么卵用，不过还是配置一下比较好）  
设置redirect参数:该设置是当有GFW的机器扫描你的服务器后，会自动跳转到你配置的网站，如果配置多个，会随机挑选一个跳转！**  

<img src="https://github.com/smallqiangno/use-guide/blob/master/server/serverResistance1.png" width="1348" height="622" alt="图片加载失败时，显示这段字"/>  

### 二.禁用掉一直在莫名扫描你的服务器的机器IP  
**有人会问，GFW真的一直在扫描我的机器吗？  
这个我不能完全确定，我的经历是这样的：一开始有大量的大陆IP一直在扫描我的机器，后来我禁掉这些IP后，又都变成荷兰和美国两个地方的IP了(严重怀疑是伪装成这两个国家的IP....)，我觉得应该没有谁那么闲一直在访问我的机器.....**

<img src="https://github.com/smallqiangno/use-guide/blob/master/server/serverResistance2.png" width="1141" height="413" alt="图片加载失败时，显示这段字"/>   

**解决方案：启动防火墙，然后执行ssr安装目录下的utils目录下的autoban.py脚本，通过防火墙禁掉这些IP！  
 原脚本的禁用规则是不可用的，所以我修改了一下原脚本，需要的可以去下载！（这个脚本采用的是firewalld防火墙，一般centos7以上的操作系统用的都是该防火墙）**
 执行脚本命令：
 ```
 python autoban.py < ../ssserver.log
 ```
[脚本下载](https://github.com/smallqiangno/use-guide/blob/master/server/autoban.py)










