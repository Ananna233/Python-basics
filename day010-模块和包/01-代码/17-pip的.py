# 下面 Terminal(终端) 点开
# 命令
# 安装：pip install +包名字  # pip install flask
# 卸载：pip uninstall +包名字  # pip uninstall flask
# 查看安装的第三方模块：pip list



# 下载安装一个包
# D:\Python基础学习\day010-模块和包\01-代码>pip install flask
# Collecting flask
#   Downloading Flask-1.1.2-py2.py3-none-any.whl (94 kB)
#      |████████████████████████████████| 94 kB 280 kB/s
# Collecting click>=5.1
#   Downloading click-7.1.2-py2.py3-none-any.whl (82 kB)
#      |████████████████████████████████| 82 kB 416 kB/s
# Collecting Werkzeug>=0.15
#   Downloading Werkzeug-1.0.1-py2.py3-none-any.whl (298 kB)
#      |████████████████████████████████| 298 kB 3.3 MB/s
# Collecting Jinja2>=2.10.1
#   Downloading Jinja2-2.11.2-py2.py3-none-any.whl (125 kB)
#      |████████████████████████████████| 125 kB 6.8 MB/s
# Collecting itsdangerous>=0.24
#   Downloading itsdangerous-1.1.0-py2.py3-none-any.whl (16 kB)
# Collecting MarkupSafe>=0.23
#   Downloading MarkupSafe-1.1.1-cp38-cp38-win_amd64.whl (16 kB)
# Installing collected packages: click, Werkzeug, MarkupSafe, Jinja2, itsdangerous, flask
# Successfully installed Jinja2-2.11.2 MarkupSafe-1.1.1 Werkzeug-1.0.1 click-7.1.2 flask-1.1.2 itsdangerous-1.1.0
# WARNING: You are using pip version 20.1.1; however, version 20.2.3 is available.
# You should consider upgrading via the 'd:\python\python.exe -m pip install --upgrade pip' command.


# 路径是  ../python/lib/site-packages??


# 卸载一个包
# D:\Python基础学习\day010-模块和包\01-代码>pip uninstall flask
# Found existing installation: Flask 1.1.2
# Uninstalling Flask-1.1.2:
#   Would remove:
#     d:\python\lib\site-packages\flask-1.1.2.dist-info\*
#     d:\python\lib\site-packages\flask\*
#     d:\python\scripts\flask.exe
# Proceed (y/n)? y
#   Successfully uninstalled Flask-1.1.2
#
# D:\Python基础学习\day010-模块和包\01-代码>


# 查看安装的第三方模块：pip list
# D:\Python基础学习\day010-模块和包\01-代码>pip list
# Package                Version
# ---------------------- -------
# click                  7.1.2
# itsdangerous           1.1.0
# Jinja2                 2.11.2
# MarkupSafe             1.1.1
# mysql-connector-python 8.0.21
# pip                    20.1.1
# setuptools             47.1.0
# Werkzeug               1.0.1
# WARNING: You are using pip version 20.1.1; however, version 20.2.3 is available.
# You should consider upgrading via the 'd:\python\python.exe -m pip install --upgrade pip' command.



# D:\Python基础学习\day010-模块和包\01-代码>pip freeze > requirements.txt
# pip freeze > file_name  将安装的模块和版本号重定向输出到指定的文件
# pip install -r file_name 读取文件里的模块号和版本号并安装
