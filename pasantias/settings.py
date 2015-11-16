"""
Django settings for pasantias project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
from unipath import Path
BASE_DIR = Path(__file__).ancestor(2)

MI_DOMINIO="localhost:8000"


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '$f^lo$q$76fs8$5^ebtn89!z$=y**a&&mbppis6ghs8w2d0dlh'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
DEBUG404 = DEBUG
TEMPLATE_DEBUG = False

ALLOWED_HOSTS = ['localhost','127.0.0.1']


# Application definition

# Application definition
DJANGO_APPS=(
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    )

THIRD_PARTY_PATY_APPS=(
    'social.apps.django_app.default',
    'disqus',
    'django_cleanup',
    )
LOCAL_APPS=(
       'apps.manager',       
    )


INSTALLED_APPS = DJANGO_APPS+THIRD_PARTY_PATY_APPS+LOCAL_APPS


MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'pasantias.urls'

WSGI_APPLICATION = 'pasantias.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'mibd',
        'USER':'miuser',
        'PASSWORD': 'mipass'
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'es-Es'

TIME_ZONE = 'America/Lima'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/
STATIC_ROOT = '/static/'
STATIC_URL = '/static/'
#Direccion de cargas como imagenes de usuarios 
MEDIA_ROOT=os.path.join(BASE_DIR, 'uploads/')
MEDIA_URL="/uploads/"
#Direccion  de los archivos del sitio css,js,img
STATICFILES_DIRS=[BASE_DIR.child('static')]
#En donde van a estar alojados mis templates
TEMPLATE_DIRS=(
    BASE_DIR.child('templates'),
    )


from django.conf.global_settings import TEMPLATE_CONTEXT_PROCESSORS as TCP

TEMPLATE_CONTEXT_PROCESSORS = TCP+(
    'django.contrib.auth.context_processors.auth',
    'social.apps.django_app.context_processors.backends',
    'social.apps.django_app.context_processors.login_redirect',
    'django.core.context_processors.request',
    'apps.manager.context_processors.ejemplo',
    'apps.manager.context_processors.miscategorias',
    'apps.manager.context_processors.misentradas',
    'apps.manager.context_processors.userpersonalizado',
)
SOCIAL_AUTH_PIPELINE = (
        'social.pipeline.social_auth.social_details',
        'social.pipeline.social_auth.social_uid',
        'social.pipeline.social_auth.auth_allowed',
        'social.pipeline.social_auth.social_user',
        'social.pipeline.user.get_username',
        'social.pipeline.user.create_user',
        'social.pipeline.social_auth.associate_user',
        'social.pipeline.social_auth.load_extra_data',
        'social.pipeline.user.user_details',
        'apps.manager.pipelines.login',
    )
AUTHENTICATION_BACKENDS = (
    'social.backends.facebook.FacebookAppOAuth2',
    'social.backends.facebook.FacebookOAuth2',
    'social.backends.twitter.TwitterOAuth',
    'django.contrib.auth.backends.ModelBackend',
    )
SOCIAL_AUTH_LOGIN_URL = "/url_de_logueo/"
SOCIAL_AUTH_LOGIN_REDIRECT_URL='/'
SOCIAL_AUTH_LOGIN_ERROR_URL = '/'



SOCIAL_AUTH_FACEBOOK_PROFILE_EXTRA_PARAMS = {
  'locale': 'en_US',
  'fields': 'id, name, email, age_range'
}
SOCIAL_AUTH_FACEBOOK_SCOPE = ['email',

'publish_actions',
#'read_stream',
#'publish_stream',
#'offline_access',
#'user_photos',
]


SITE_ID = 1


from django.core.urlresolvers import reverse_lazy 
LOGIN_URL = reverse_lazy('milogin')
LOGIN_REDIRECT_URL=reverse_lazy('home')

SOCIAL_AUTH_FACEBOOK_KEY='mifacekey'
SOCIAL_AUTH_FACEBOOK_SECRET='mifacekey'
DISQUS_API_KEY = 'midisqusapi'
DISQUS_WEBSITE_SHORTNAME = 'blapp'