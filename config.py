import os

class Config:
   
    SECRET_KEY = 'PatrickNgare'
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://patel:12345@localhost/pate'
    UPLOADED_PHOTOS_DEST ='app/static/photos'
    
   

    # simple mde  configurations
    SIMPLEMDE_JS_IIFE = True
    SIMPLEMDE_USE_CDN = True

class TestConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://patel:12345@localhost/pate'


class ProdConfig(Config):
    
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")
   

    
class DevConfig(Config):
   

    

    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig,
'test':TestConfig
}