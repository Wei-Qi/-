""""
config -
Author：wiki
Date：2022/5/6
"""


from config_local import *  # 在config_local中执行本地数据库的配置,git时忽略config_local文件

# 服务器暂时没有实现
# HOSTNAME = '43.138.58.223'
# PORT = '3306'
# DATABASE = 'ditanhuo'
# USERNAME = 'ditanhuo'
# PASSWORD = 'byeWxAmAH8DHp5Fb'
DB_URI = 'mysql+pymysql://{}:{}@{}:{}/{}?charset=utf8'.format(USERNAME, PASSWORD, HOSTNAME, PORT, DATABASE)
SQLALCHEMY_DATABASE_URI = DB_URI
SQLALCHEMY_TRACK_MODIFICATIONS = True
#启动CSRF保护
CSRF_ENABLED = True
SECRET_KEY = '123ijlks_]dja2_su?s/s*62%%#456'
# 邮箱配置
# 项目中用的是QQ邮箱
MAIL_SERVER = 'smtp.qq.com'
MAIL_PORT = 465
MAIL_USE_TLS = False
MAIL_USE_SSL = True
MAIL_DEBUG = True
MAIL_USERNAME = '2432097997@qq.com'
MAIL_PASSWORD = 'ddupplxslkgpdibi'
MAIL_DEFAULT_SENDER = '2432097997@qq.com'

LocalAddress='http://127.0.0.1:5000'