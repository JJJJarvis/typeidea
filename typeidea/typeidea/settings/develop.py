from .base import * #NOQA

DEBUG = True

DATABASES = {
    'default':{
        'ENGINE':'',
        'NAME':os.path.join(BASE_DIR,'db.sqlite3'),
        }
    } 
