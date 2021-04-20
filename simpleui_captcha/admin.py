from django.contrib import admin

from .forms import MultiCaptchaAdminAuthenticationForm

admin.AdminSite.login_form = MultiCaptchaAdminAuthenticationForm