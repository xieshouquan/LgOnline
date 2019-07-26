from django.db import models

from users.models import UserProfile
from courses.models import Course
# Create your models here.


class UserAsk(models.Model):
    name=models.CharField("姓名",max_length=20)
    mobile=models.CharField("手机号码",max_length=11)
    course_name=models.CharField("课程名",max_length=50)
    create_time=models.DateTimeField("添加时间",auto_now_add=True)

    class Meta:
        verbose_name="用户咨询"
        verbose_name_plural=verbose_name


class CourseComments(models.Model):
    # 课程评论
    user=models.ForeignKey(UserProfile,"用户",on_delete=models.CASCADE)
    course=models.ForeignKey(Course,"课程",on_delete=models.CASCADE)
    comments=models.CharField("评论",max_length=200)
    create_time=models.DateTimeField("添加时间",auto_now_add=True)

    class Meta:
        verbose_name="用户评论"
        verbose_name_plural=verbose_name


class UserFavorite(models.Model):
    user=models.ForeignKey(UserProfile,"用户",on_delete=models.CASCADE)
    fav_id=models.IntegerField("数据id",default=0)
    fav_type=models.IntegerField("收藏类型",choices=((1,"课程"),(2,"课程机构"),(3,"讲师")),default=1)
    create_time=models.DateTimeField("添加时间",auto_now_add=True)

    class Meta:
        verbose_name="用户收藏"
        verbose_name_plural=verbose_name


class UserMessage(models.Model):
    user=models.IntegerField("接收用户",default=0)
    comments=models.CharField("消息内容",max_length=500)
    has_read=models.BooleanField("是否已读",default=False)
    create_time=models.DateTimeField("添加时间",auto_now_add=True)

    class Meta:
        verbose_name="用户消息"
        verbose_name_plural=verbose_name


class UserCourse(models.Model):
    user=models.ForeignKey(UserProfile,"用户",on_delete=models.CASCADE)
    course=models.ForeignKey(Course,"课程",on_delete=models.CASCADE)
    create_time=models.DateTimeField("添加时间",auto_now_add=True)

    class Meta:
        verbose_name="用户课程"
        verbose_name_plural=verbose_name
