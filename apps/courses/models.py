from django.db import models
from organization.models import CourseOrg

# Create your models here.


class Course(models.Model):
    course_org = models.ForeignKey(CourseOrg,verbose_name="课程机构",null=True,blank=True,on_delete=models.CASCADE)
    name = models.CharField(verbose_name="课程名", max_length=50)
    desc = models.CharField(verbose_name="课程描述", max_length=300)
    detail = models.TextField(verbose_name="课程详情")
    degree = models.CharField(verbose_name="难度", choices=(("cj", "初级"), ("zj", "中级"), ("gj", "高级")), max_length=2)
    learn_times = models.IntegerField(verbose_name="学习时长(分钟数)", default=0)
    students = models.IntegerField(verbose_name="学习人数", default=0)
    fav_nums = models.IntegerField(verbose_name="收藏人数", default=0)
    image = models.ImageField(verbose_name="封面图", upload_to="courses/%Y/%m", max_length=100)
    click_nums = models.IntegerField(verbose_name="点击数", default=0)
    create_time = models.DateTimeField(verbose_name="添加时间", auto_now_add=True)

    class Meta:
        verbose_name = "课程"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Lesson(models.Model):
    course = models.ForeignKey(Course, verbose_name="课程名称", on_delete=models.CASCADE)
    name = models.CharField(verbose_name="章节名", max_length=100)
    create_time = models.DateTimeField(verbose_name="添加时间", auto_created=True)

    class Meta:
        verbose_name = "章节"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Video(models.Model):
    lesson = models.ForeignKey(Lesson, verbose_name="章节", on_delete=models.CASCADE)
    name = models.CharField(verbose_name="视频名", max_length=100)
    create_time = models.DateTimeField(verbose_name="添加时间", auto_created=True)

    class Meta:
        verbose_name = "视频"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class CourseResource(models.Model):
    course = models.ForeignKey(Course, verbose_name="课程", on_delete=models.CASCADE)
    name = models.CharField(verbose_name="名称", max_length=100)
    download = models.FileField(verbose_name="资源文件", upload_to="course/resourse/%Y/%m", max_length=100)
    create_time = models.DateTimeField(verbose_name="添加时间", auto_created=True)

    class Meta:
        verbose_name = "课程资源"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name
