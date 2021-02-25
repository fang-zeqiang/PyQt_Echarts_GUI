# 教程

[English](/README.md)   [中文版](/README-CN.md)

---

这里是结合ECharts的Python图形用户界面的开源项目
通过测试可用的操作系统有MacOS BigSur, Windows 10
该教程以MacOS系统上实现为例子，这里的终端在Windows里为PowerShell或者Git Bash

总共四步，即可快速构建可视化程序！

## Step1: 安装Git环境（可选）

- 访问Git官网安装对应操作系统的Git环境

- 然后你只需要输入以下代码在终端就可以克隆我的项目
  
  ```bash
  git clone https://github.com/Hereislittlemushroom/PyQt_Echarts_GUI.git
  ```

- 如果不想安装Git, 只需要右上角点击Download按钮

## Step2: 安装依赖环境

- 安装 python3.7 

- 使用[pip]([Python pip 安装与使用 | 菜鸟教程 (runoob.com)](https://www.runoob.com/w3cnote/python-pip-install-usage.html))命令安装以下包，如果因网络原因安装不成功可以在[这个目录](/site-packages)下找到对应包手动安装
  
  1. PyQt5 (不用担心PyQt5的版本问题，保持大小写进行安装)
  
  2. pyecharts==0.5.11 （注意pyecharts的版本号）
  
  3. PyQtWebEngine
     
     ```bash
     pip3 install PyQt5
     pip3 install PyQtWebEngine
     pip3 install pyecharts==0.5.11
     ```

## Step3: 检查文件完整性

- templete.html （放置渲染ECharts图表的文件）

- echarts.min.js （官方的JS包）

- start.py （GUI启动程序）

## Step4: 启动脚本

- 打开终端
  
  输入以下代码来启动程序
  
  ```bash
    cd PyQt_Echarts_GUI
    python3 start.py
  ```

## 最终效果

### 1. 图表类型间的相互切换

![效果4](/img/image32.gif)

### 2. 桑基图呈现

![效果3](/img/image34.gif)

### 3. 柱图线图切换呈现

![效果1](/img/image36.gif)

### 4. 雷达图呈现

![效果2](/img/image35.gif)

## 参考资料

[PyQt Tutorial](https://www.cnblogs.com/archisama/p/5442071.html)

[Original Project](https://blog.csdn.net/this_is_id/article/details/86688585)

[Trick of Trades](https://zhidao.baidu.com/question/538702856.html)
