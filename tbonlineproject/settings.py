# Django settings for testdjango project.


import os

try:
    from local_settings import APP_NAME, COMMENTS_APP
except ImportError:
    APP_NAME = "tb"
    COMMENTS_APP = "CommentRecaptcha"


DEBUG = False
TEMPLATE_DEBUG = DEBUG


SITE_ROOT = os.path.dirname(os.path.realpath(__file__))


ADMINS = (
          ('Administrator', 'info@tbonline.info'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': os.path.join(SITE_ROOT, 'tbonline.sqlite'),                      # Or path to database file if using sqlite3.
        'USER': '',                      # Not used with sqlite3.
        'PASSWORD': '',                  # Not used with sqlite3.
        'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
    }
}

EMAIL_HOST = 'smtp.webfaction.com'
EMAIL_HOST_USER = 'tbcab'
EMAIL_HOST_PASSWORD = '12345'
DEFAULT_FROM_EMAIL = 'info@tbonline.info'
# SERVER_EMAIL = 'info@tbonline.info'

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# On Unix systems, a value of None will cause Django to use the same
# timezone as the operating system.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'Africa/Johannesburg'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale
USE_L10N = True



# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.lawrence.com/media/"
MEDIA_ROOT = os.path.join(SITE_ROOT, 'media')

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://media.lawrence.com/media/", "http://example.com/media/"
MEDIA_URL = '/media/'

THUMBNAIL_DEBUG = True

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/home/media/media.lawrence.com/static/"
STATIC_ROOT = os.path.join(SITE_ROOT, 'static')

# URL prefix for static files.
# Example: "http://media.lawrence.com/static/"
STATIC_URL = '/static/'

# URL prefix for admin static files -- CSS, JavaScript and images.
# Make sure to use a trailing slash.
# Examples: "http://foo.com/static/admin/", "/static/admin/".
ADMIN_MEDIA_PREFIX = STATIC_URL + "grappelli/"

# Additional locations of static files
STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    #'/usr/local/lib/python2.6/dist-packages/filebrowser/media',
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = '_)(+!6a28nsv%+f$ktmeo1a21&v=%bp=yk-tyxnh_1k*(3$0%#'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',
    'accounts.middleware.AutoLogoutMiddleware',
    'accounts.middleware.WebfactionFixMiddleware',
    )


ROOT_URLCONF = 'tbonlineproject.urls'

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    os.path.join(os.path.join(SITE_ROOT, APP_NAME),'templates'),
    os.path.join(SITE_ROOT, 'templates'),
    os.path.join(SITE_ROOT, 'post/templates'),
    os.path.join(SITE_ROOT, 'gallery/templates'),
    os.path.join(SITE_ROOT, 'feeder/templates'),
    os.path.join(SITE_ROOT, 'copyright/templates'),
    os.path.join(SITE_ROOT, 'notifications/templates'),
    os.path.join(SITE_ROOT, 'tweets/templates'),
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.markup',
    'django.contrib.comments',
    'django.contrib.flatpages',
    'sorl.thumbnail',
    'contact_form',
    'grappelli',
    'filebrowser',
    'django.contrib.admin',
    'django.contrib.admindocs',
    'django.contrib.sitemaps',
    'south',
    'faq',
    'registration',
    'tagging',
    'copyright',
    'credit',
    'relatedcontent',
    'gallery',
    'feeder',
    'archive',
    'enhancedtext',
    'categories',
    'post',
    'story',
    'tagviews',
    'notifications',
    'tweets',
    'RegistrationRecaptcha',
    'userprofiles',
    COMMENTS_APP,
    APP_NAME,
)

AUTHENTICATION_BACKENDS = (
    'accounts.backends.EmailOrUsernameModelBackend',
    'django.contrib.auth.backends.ModelBackend'
)

TWEETS_ACTIVATED = True

GRAPPELLI_ADMIN_TITLE = '<a href="/">TB Online</a> Administration'

ACCOUNT_ACTIVATION_DAYS = 2
LOGIN_REDIRECT_URL = '/'

HAYSTACK_SITECONF = 'tbonlineproject.search_sites'
HAYSTACK_SEARCH_ENGINE = 'xapian'
#HAYSTACK_WHOOSH_PATH = os.path.join(SITE_ROOT, 'whoosh_search_index')
HAYSTACK_XAPIAN_PATH = os.path.join(SITE_ROOT, 'xapian_search_index')

RECAPTCHA_PUBLIC_KEY = '6LeMQsoSAAAAAP5BQhOF0kuPCPvtwwu_9AYshPMA'
RECAPTCHA_PRIVATE_KEY = '6LeMQsoSAAAAAGrrDr05Uyhoh7DJHHsArD4BNXmA'

MAX_NUM_IMAGES = 10

#The time in MINUTES that the homepage and posts views will be cached
CACHE_TIME = 0

CACHES = {
#    'default': {
#        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
#        'LOCATION': 'unix:/home/tbcab/memcached.sock'
#    }
}

TEMPLATE_CONTEXT_PROCESSORS = ("django.contrib.auth.context_processors.auth",
                               "django.core.context_processors.debug",
                               "django.core.context_processors.i18n",
                               "django.core.context_processors.media",
                               "django.core.context_processors.static",
                               "django.core.context_processors.request",
                               "django.contrib.messages.context_processors.messages",
                               "post.context_processors.current_site")


# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}

AUTH_PROFILE_MODULE = 'auth.User'

# Mailchimp settings
MAILCHIMP_KEY = 'ba62b7f0b188051d29344063caba744b-us11'
LIST_ID = 'ae7bcd30bb'

try:
    import local_settings
    from local_settings import *
except ImportError:
    pass
else:
    PROJECT_TEMPLATE_DIR = getattr(local_settings, "PROJECT_TEMPLATE_DIR", None)

    if PROJECT_TEMPLATE_DIR:
        TEMPLATE_DIRS =  (PROJECT_TEMPLATE_DIR,) + TEMPLATE_DIRS
