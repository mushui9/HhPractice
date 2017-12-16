# BiliClick
## 0
### python学习笔记,获取B站点击百万视频；编程初学者经验,$ 开始后为代码

1. 首先去官网找一个适合系统的版本下载，官网也是一份教程，看官网步骤安装
* http://docs.python-guide.org/en/latest/starting/installation/

2. 添加环境，win+R输入cmd打开powershell命令行，
* 输入$ [Environment]::SetEnvironmentVariable("Path", "$env:Path;C:\Python36\;C:\Python36\Scripts\", "User")

3. 安装setuptools和pip，用python解释器运行官网给的脚本文件即可(ez_setup.py,get_pip.py)
* 解释器是执行.py文件的程序，如CPython，IPython，PyPy等；
* 编辑器是一个IDE，用来编写代码的，如安装自带的IDLE，pycharm等。

4. 安装库文件，在powershell命令行中输入$ pip install lib_name
* 需要用到requests,beautifulsoup4

5. 编写并运行BiliClick.py，简单获取B站点击百万的视频：
* 编写代码过程是一边学习一边调试的过程，不会的就在网上搜索（已经有好多人做过了）
* 爬取效率特别低，其实网页很简单，或许用re更好一些
* 主要是学习bs库，复杂网页还是bs更简单一些；
* B站视频编号比较简单，但具体的编号规则不清楚，直接从0向后循环了
* 爬取结果在click_num.txt里，不时更新

# BiliClick2+mysql;3+pool
## 1
### 爬取B站点击百万视频升级版，获取更多参数，多进程，存入数据库，外部控制无限循环退出

1. 安装库文件PyMySQL
* 安装MySQL，我是学习PHP时安装phpStudy一并安装的
* PyMySQL用于python3.x连接MySQL服务器，python2中则使用mysqldb
* 从数据库中读取上一次爬取的number

2. 解析B站网址
* 查询B站api提交网页，在下面网址找到数据，已经简化过
* <http://api.bilibili.com/x/web-interface/archive/stat?aid=2479227>

3. 使用requests.get(url).json()['data']获取详细数据
* 使用try……except……结构去除空视频和无效数据

4. 如果view量大于百万从主站获取标题并写入数据库，通过option标签过滤多个分P的情况

5. 通过读取数据库中某值判断是否结束，控制循环退出

6. 用Pool.map多进程处理

7. 存入爬到的number下次读取，关闭数据库