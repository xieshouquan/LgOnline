from django import forms
from captcha.fields import CaptchaField


class LoginForm(forms.Form):
    username = forms.CharField(required=True)
    password = forms.CharField(required=True, min_length=5)


class RegisterForm(forms.Form):
    email = forms.EmailField(required=True)
    password = forms.CharField(required=True, min_length=5)
    captcha = CaptchaField(required=True, error_messages={'invalid': '验证码错误'})


class ForgetForm(forms.Form):
    email = forms.EmailField(required=True)
    captcha = CaptchaField(required=True, error_messages={'invalid': '验证码错误'})


class ModifyPwdForm(forms.Form):
    password = forms.CharField(required=True, min_length=5)
    password2 = forms.CharField(required=True, min_length=5)
