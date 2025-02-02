import os


class Config:
    '''
    General configuration parent class
    '''

    NEWS_API_BASE_URL ='https://newsapi.org/v2/sources?apiKey=b4cd697d9d1644d394ba25d5a93875ab'
    ARTICLE_API_BASE_URL='https://newsapi.org/v2/everything?q={}&apiKey=b4cd697d9d1644d394ba25d5a93875ab'
    
    NEWS_API_KEY = os.environ.get('NEWS_API_KEY')


class ProdConfig(Config):
    '''
    Production  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    pass


class DevConfig(Config):
    '''
    Development  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''

    DEBUG = True


config_options = {
    'development': DevConfig,
    'production': ProdConfig
}