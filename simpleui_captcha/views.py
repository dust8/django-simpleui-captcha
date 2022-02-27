from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View

from .forms import CaptchaLoginForm
from .settings import dsc_settings


class LoginWithCaptcha(View):
    def get(self, request):
        failed_login_count = request.session.get(dsc_settings.FAILED_LOGIN_COUNT_NAME, 0)
        if failed_login_count >= dsc_settings.MAX_FAILED_LOGIN_COUNT:
            form = CaptchaLoginForm(request.POST)
        else:
            form = AuthenticationForm()

        return render(request, 'admin/login.html', {'form': form})

    def post(self, request):
        failed_login_count = request.session.get(dsc_settings.FAILED_LOGIN_COUNT_NAME, 0)
        if failed_login_count >= dsc_settings.MAX_FAILED_LOGIN_COUNT:
            form = CaptchaLoginForm(data=request.POST)
        else:
            form = AuthenticationForm(data=request.POST)

        if form.is_valid():
            request.session[dsc_settings.FAILED_LOGIN_COUNT_NAME] = 0
            user = authenticate(username=form.cleaned_data["username"], password=form.cleaned_data["password"])
            if user is not None:
                login(request, user)
                return HttpResponseRedirect(reverse_lazy('admin:index'))
        else:
            failed_login_count += 1
            request.session[dsc_settings.FAILED_LOGIN_COUNT_NAME] = failed_login_count
            if failed_login_count >= dsc_settings.MAX_FAILED_LOGIN_COUNT:
                form = CaptchaLoginForm(request.POST)
            messages.add_message(request, messages.INFO, 'Not a valid request')

        return render(request, 'admin/login.html', {'form': form})
