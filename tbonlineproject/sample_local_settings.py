import os

SITE_ROOT = os.path.dirname(os.path.realpath(__file__))

STATIC_ROOT = ''

STATICFILES_DIRS = (
    os.path.join(SITE_ROOT, 'static'),
)

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(SITE_ROOT, 'tbonline_local.sqlite'),
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
    }
}

HAYSTACK_SEARCH_ENGINE = 'simple'