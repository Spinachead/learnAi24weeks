# 安装anaconda并且配置pytorch环境
## conda常用命令
- conda env list
- conda create -n torch_env python=3.10
- conda activate torch_env
- conda install pytorch (无cpu)
- conda install jupyterlab
- conda install ipykernel (为jupyter安装内核支持 确保jupyter能识别当前环境)
- jupyter lab (启动jupyter lab)


## python中两个常用的工具函数
- dir()
- help()

## 配置环境遇到的坑
- 使用pycharm创建新项目时要选择conda安装目录下的env文件夹下对应pytorch中的python.exe, 不能直接选择conda安装文件夹下的pyton.exe 不然会引入不了torch
- 安装完jupyterlab后一定要安装内核ipykernel
