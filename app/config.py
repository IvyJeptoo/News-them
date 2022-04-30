class Config:
    '''
    General configuration parent class
    '''
    pass
    # MOVIE_API_BASE_URL ='https://api.themoviedb.org/3/movie/{}?api_key={}'

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