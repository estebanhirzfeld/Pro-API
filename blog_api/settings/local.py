from .base import * # noqa
from .base import env
# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env("DJANGO_SECRET_KEY",
                default="django-insecure-29gyb&z9c9lcr+)#fu$mwu&w_(&wdxmq9ylm_jeggz_767x-gd"
)

# python3 -c """import secrets; print(secrets.token_urlsafe(38))"""


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env.bool("DJANGO_DEBUG", True)

DOMAIN = env("DOMAIN")

CSRF_TRUSTED_ORIGINS = ["http://localhost:8080"]