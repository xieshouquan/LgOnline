from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.db import models
# from datetime import datetime
# Create your models here.


class MyUserManager(BaseUserManager):
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
    is_delete=models.BooleanField(default=False,verbose_name='逻辑删除', help_text='逻辑删除')

    objects = MyUserManager()

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

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin

    class Meta:
        verbose_name="用户信息"
        verbose_name_plural=verbose_name


class EmailVerifyRecord(models.Model):
    code=models.CharField(verbose_name="验证码",max_length=20)
    email=models.EmailField(verbose_name="邮箱",max_length=50)
    send_type=models.CharField(choices=(("register","注册"),("forget","找回密码")),max_length=10)
    send_time=models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name="邮箱验证码"
        verbose_name_plural=verbose_name


class Banner(models.Model):
    title=models.CharField(verbose_name="标题",max_length=100)
    image=models.ImageField(verbose_name="轮播图",upload_to="banner/%Y/%m",max_length=100)
    url=models.URLField(verbose_name="访问地址",max_length=200)
    index=models.IntegerField(verbose_name="顺序",default=100)
    add_time=models.DateTimeField(verbose_name="添加时间",auto_now=True)

    class Meta:
        verbose_name="轮播图"
        verbose_name_plural=verbose_name
