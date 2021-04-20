from django.urls import path, include

urlpatterns = [
    path('captcha/', include('captcha.urls')),
]
