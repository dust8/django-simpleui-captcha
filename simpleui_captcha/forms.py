from captcha.fields import CaptchaField
from django.contrib.admin.forms import AdminAuthenticationForm


class MultiCaptchaAdminAuthenticationForm(AdminAuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['captcha'] = CaptchaField()
