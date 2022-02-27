# django-simpleui-captcha
[![PyPI version](https://badge.fury.io/py/django-simpleui-captcha.svg)](https://badge.fury.io/py/django-simpleui-captcha)

django-simpleui-captcha 是一个 django 后台管理登录验证码插件

## 界面
![image](screenshoot/screenshoot1.png)

## 安装
```
pip install django-simpleui-captcha
```

### 依赖
- Django
- django-simple-captcha

## 快速开始
### 1. 添加 "simpleui_captcha" 到 INSTALLED_APPS 设置, 注意要放在最前面
```py
INSTALLED_APPS = [
    "simpleui_captcha",
    "simpleui",
    ... 
]
```

### 2. 添加 `simpleui_captcha` 的 `url` 到你的项目 `urls.py` ::
```py
path('simpleui_captcha/', include('simpleui_captcha.urls')),
```

### 3. 运行 `python manage.py migrate` 迁移验证码模型

### 4.(可选)后台在连续登录n次失败后,要求输入验证码登录
```py
# urls.py
from simpleui_captcha.views import LoginWithCaptcha


urlpatterns = [
    path('admin/login/', LoginWithCaptcha.as_view(), name='admin_login'),
    path('admin/', admin.site.urls),
    ...
]

# settings.py 默认值
SIMPLEUI_CAPTCHA = {
    'FAILED_LOGIN_COUNT_NAME': 'failed_login_count', # session 的键名
    'MAX_FAILED_LOGIN_COUNT': 3, # 不需要输验证码的最大失败次数
}
```
