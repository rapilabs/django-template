import cbs
import dj_database_url


class BaseSettings(cbs.BaseSettings):
    PROJECT_NAME = 'django_template'
    SITE_ID = 1
    DATABASES = {
        'default': dj_database_url.config()
    }
    TEMPLATE_CONTEXT_PROCESSORS = (

        # Required by allauth template tags
        "django.core.context_processors.request",

        # allauth specific context processors
        "allauth.account.context_processors.account",
        "allauth.socialaccount.context_processors.socialaccount",

        "django.contrib.auth.context_processors.auth",
    )
    AUTHENTICATION_BACKENDS = (
        # Needed to login by username in Django admin, regardless of `allauth`
        "django.contrib.auth.backends.ModelBackend",
        # `allauth` specific authentication methods, such as login by e-mail
        "allauth.account.auth_backends.AuthenticationBackend",
    )

    def INSTALLED_APPS(self):
        return self.INSTALLED_APPS + (
            'allauth',
            'allauth.account',
            'allauth.socialaccount',
            'allauth.socialaccount.providers.google',
            'rest_framework',
        )

    # django-allauth
    ACCOUNT_AUTHENTICATION_METHOD = 'email'
    ACCOUNT_USERNAME_REQUIRED = False
    ACCOUNT_EMAIL_REQUIRED = True
    ACCOUNT_USER_MODEL_USERNAME_FIELD = None
    ACCOUNT_EMAIL_VERIFICATION = 'mandatory'
    LOGIN_REDIRECT_URL = '/'


class LocalSettings(BaseSettings):

    def INSTALLED_APPS(self):
        return self.INSTALLED_APPS + (
            'django_admin_generator',
            'django_rest_framework_generator',
        )


class ProductionSettings(BaseSettings):
    DEBUG = False
    # ALLOWED_HOSTS = [
    #     'your.domain.here',
    # ]

    # Security settings
    SECURE_SSL_REDIRECT = True
    SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

    # django-allauth
    ACCOUNT_DEFAULT_HTTP_PROTOCOL = 'https'


MODE = os.environ.get('DJANGO_MODE', 'Local')
cbs.apply('{}Settings'.format(MODE.title()), globals())
