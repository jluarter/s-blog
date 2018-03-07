from os import path
#获取当前文件的绝对路径
basedir= path.abspath(path.dirname(__file__))

class Config(object):
    '''基本配置'''
    pass

class UserConfig(Config):
    '''用户配置 '''
    pass

class DevConfig(Config):
    '''开发配置'''
    DEBUG=True
    # 拼接数据库的ＵＲＬ路径
    # path.join　把basedir和data.sqlite的路径拼接起来#
    # data.sqlite为数据库文件，若该文件夹下没有这个文件会自动创建
    SQLALCHEMY_DATABASE_URI='sqlite:///'+ path.join(basedir,'data.sqlite')