import os
SECRET_KEY = 'secret_key'


DEBUG = False

ALLOWED_HOSTS = ["127.0.0.1"]

# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": "db_m1",
        "USER": "postgres",
        "PASSWORD": "postgres",
        "HOST": "127.0.0.1",
        "PORT": "5432",
    }
}

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

#STATIC_URL = 'static/'

#STATICFILES_DIRS = [
    #BASE_DIR / "static",
    #'/var/www/static/',
#]

STATIC_ROOT = os.path.join(BASE_DIR, 'static')
