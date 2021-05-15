class Base_Config:
     SECRET_KEY     = "ff34m-fg5gpxq"
     UPLOAD_FOLDER  = "static/images"
     DEBUG          = True
     MAIL_VER_CODE = "0000"
     MAIL_SERVER    ='smtp.gmail.com'
     MAIL_PORT      = 465
     MAIL_USERNAME  = 'x.admns@gmail.com'
     MAIL_PASSWORD  = 'A444z444'
     MAIL_USE_TLS   = False
     MAIL_USE_SSL   = True
     MAIL_DEFAULT_SENDER='x.admns@gmail.com'

class Prod_Config(Base_Config):
     FLASK_ENV      = "production"
     DEBUG          = False

class Dev_Config(Base_Config):
     FLASK_ENV      = "development"   
     
     
