DATABASES = {
    'default': {
        'ENGINE': 'firebird',
        'NAME':'base.fdb',
        'USER':'usuario1',
        'PASSWORD':'bolita1',
        'HOST':'localhost',
        'PORT':'3050',
        'OPTIONS': {
            'charset': 'UTF8',
        },
    }
}
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'pets2',
]