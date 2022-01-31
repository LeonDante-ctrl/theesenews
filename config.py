import os

class Config:
    '''
    General configuration parent class
    '''
    @staticmethod
    def init_app(app):
            pass
  


class ProdConfig(Config):
    '''
    Production  configuration child class
    '''
    pass


class DevConfig(Config):
    '''
    Development  configuration child class
    '''

    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig
}