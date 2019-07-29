from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from django.db import models
# from datetime import datetime
# Create your models here.


class UserManager(BaseUserManager):
    def create_user(self, username,  password=None):
        # 验证是否有用户名
        if not username:
            raise username

        user = self.model(
            username=username
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username,  password):
        # 设置超级用户
        user = self.create_user(
            username,
            password=password
        )
        user.is_superuser=True
        user.is_admin = True
        user.save(using=self._db)
        return user

class UserProfile(AbstractBaseUser):
    username=models.CharField(verbose_name="用户名",unique=True,max_length=30)
    nick_name=models.CharField(verbose_name="昵称",max_length=50,default="")
    birday=models.DateField(verbose_name="生日",null=True,blank=True)
    gender=models.CharField(verbose_name="性别",max_length=10,choices=(("male","男"),("female","女")),default="female")
    address=models.CharField(verbose_name="联系地址",max_length=100,default="")
    mobile=models.CharField(verbose_name="电话",max_length=11,null=True,blank=True)
    image=models.ImageField(verbose_name="头像",upload_to="image/%Y/%m",default="image/default.png",max_length=100)

    creat_time=models.DateTimeField(verbose_name="注册时间",auto_now_add=True)
    update_time=models.DateTimeField(verbose_name="更新时间",auto_now=True)
    is_active = models.BooleanField(default=True)
    is_admin=models.BooleanField(default=True)
    is_staff=models.BooleanField(default=True)
    is_superuser=models.BooleanField(default=False)
    is_delete=models.BooleanField(default=False,verbose_name='逻辑删除', help_text='逻辑删除')

    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []  # 创建超级用户时使用

    def __str__(self):
        return self.username

    def delete(self, using=None, keep_parents=False):
        self.is_delete=True
        self.save()

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    class Meta:
        verbose_name="用户信息"
        verbose_name_plural=verbose_name


class EmailVerifyRecord(models.Model):
    code=models.CharField(verbose_name="验证码",max_length=20)
    email=models.EmailField(verbose_name="邮箱",max_length=50)
    send_type=models.CharField(choices=(("register","注册"),("forget","找回密码")),max_length=10,verbose_name='发送类型')
    send_time=models.DateTimeField(auto_now=True,verbose_name='发送时间')

    class Meta:
        verbose_name="邮箱验证码"
        verbose_name_plural=verbose_name

    def __str__(self):
        return self.code


class Banner(models.Model):
    title=models.CharField(verbose_name="标题",max_length=100)
    image=models.ImageField(verbose_name="轮播图",upload_to="banner/%Y/%m",max_length=100)
    url=models.URLField(verbose_name="访问地址",max_length=200)
    index=models.IntegerField(verbose_name="顺序",default=100)
    add_time=models.DateTimeField(verbose_name="添加时间",auto_now=True)

    class Meta:
        verbose_name="轮播图"
        verbose_name_plural=verbose_name

    def __str__(self):
        return self.title
