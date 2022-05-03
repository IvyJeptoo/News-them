class Config:
    '''
    General configuration parent class
    '''

    
    HEADLINES_API_BASE_URL = 'https://newsapi.org/v2/top-headlines?country=us&apiKey={}'
    SOURCES_BASE_URL = 'https://newsapi.org/v2/top-headlines/sources?apiKey={}'
    

class ProdConfig(Config):
    '''
    production config child class
    
    Args:
        config:parent config class
    '''
    pass

class DevConfig(Config):
    '''
    development config child class
    
    Args:
       config:the parent config class
    '''
DEBUG = True