import os

class Config:
    '''
    General configuration parent class
    '''
    
    NEWS_API_BASE_URL ='https://newsapi.org/v2/source?apiKey=695a759ca73b4d868c395d97269e50f6'
    ARTICLES_BASE_URL = 'https://newsapi.org/v2/everything?q=tesla&from=2022-01-01&sortBy=publishedAt&apiKey=695a759ca73b4d868c395d97269e50f6'

    NEWS_API_KEY= os.environ.get('NEWS_API_KEY')
    SECRET_KEY = os.environ.get('SECRET_KEY')
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