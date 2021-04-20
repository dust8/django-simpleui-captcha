from django.conf import settings

engine = "captcha"

if engine not in settings.INSTALLED_APPS:
    settings.INSTALLED_APPS.append(engine)
