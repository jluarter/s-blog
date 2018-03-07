class Config(object):
    '''基本配置'''
    pass

class UserConfig(Config):
    '''用户配置'''
    pass

class DevConfig(Config):
    '''开发配置'''
    DEBUG=True