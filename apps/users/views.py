from django.contrib import auth
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.backends import ModelBackend
from django.db.models import Q
# Create your views here.
from django.views import View
from django.contrib.auth.hashers import make_password

from users.forms import LoginForm, RegisterForm, ForgetForm, ModifyPwdForm
from .models import UserProfile, EmailVerifyRecord
from utils.email_send import send_register_email


class CustomBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user = UserProfile.objects.get(Q(username=username) | Q(email=username))
            if user.check_password(password):
                return user
        except Exception as e:
            return None


class ActiveUserView(View):
    def get(self, request, active_code):
        all_records = EmailVerifyRecord.objects.filter(code=active_code)
        if all_records:
            for record in all_records:
                email = record.email
                user = UserProfile.objects.get(email=email)
                user.is_active = True
                user.save()
        else:
            return render(request, 'active_fail.html')
        return render(request, 'login.html')


class RegisterView(View):
    def get(self, request):
        registerform = RegisterForm()
        return render(request, 'register.html', {'registerform': registerform})

    def post(self, request):
        registerform = RegisterForm(request.POST)
        print(registerform)
        if registerform.is_valid():
            username = request.POST.get('email')
            if UserProfile.objects.filter(email=username):
                return render(request, 'register.html', {'msg': '用户已经存在', 'registerform': registerform})
            password = request.POST.get('password')
            user = UserProfile()
            user.username = username
            user.email = username
            user.password = make_password(password)
            user.is_active = False
            user.save()
            send_register_email(username, "register")
            return render(request, 'login.html')
        else:
            return render(request, 'register.html', {'registerform': registerform})


class LoginView(View):
    def post(self, request):
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = auth.authenticate(username=username, password=password)
            if user:
                if user.is_active:
                    login(request, user)
                    return render(request, "index.html", {})
                else:
                    return render(request, 'login.html', {'msg': '用户未激活'})
            else:
                return render(request, "login.html", {'msg': '用户名或密码错误'})
        else:
            return render(request, 'login.html', {"login_form": login_form})

    def get(self, request):
        return render(request, 'login.html')


class ForgetPwdView(View):
    def get(self, request):
        forget_form = ForgetForm()
        return render(request, "forgetpwd.html", {'forget_form': forget_form})

    def post(self, request):
        forget_form = ForgetForm(request.POST)
        if forget_form.is_valid():
            email = request.POST.get('email')
            send_register_email(email, 'forget')
            return render(request, 'send_success.html')
        else:
            return render(request, "forgetpwd.html", {'forget_form': forget_form})


class ResetView(View):
    def get(self, request, active_code):
        all_records = EmailVerifyRecord.objects.filter(code=active_code)
        if all_records:
            for record in all_records:
                email = record.email
                return render(request, 'password_reset.html', {'email': email})
        else:
            return render(request, 'active_fail.html')
        return render(request, 'login.html')


class ModifyView(View):
    def post(self, request):
        modifypwdform = ModifyPwdForm(request.POST)
        if modifypwdform.is_valid():
            pwd1 = request.POST.get('password')
            pwd2 = request.POST.get('password2')
            email = request.POST.get('email')
            if pwd1 != pwd2:
                return render(request, 'password_reset.html', {"email": email, 'msg': '密码不一致'})
            user=UserProfile.objects.get(email=email)
            user.password=make_password(pwd1)
            user.save()
            return render(request, 'login.html')
        else:
            email = request.POST.get('email')
            return render(request, 'password_reset.html', {"email": email})