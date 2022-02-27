from captcha.fields import CaptchaField
from django.contrib.admin.forms import AdminAuthenticationForm
from django.contrib.auth.forms import AuthenticationForm

class MultiCaptchaAdminAuthenticationForm(AdminAuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['captcha'] = CaptchaField()


class CaptchaLoginForm(AuthenticationForm):
    captcha = CaptchaField()