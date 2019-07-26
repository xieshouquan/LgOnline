from django.db import models

# Create your models here.


class CityDict(models.Model):
    name=models.CharField("城市",max_length=20)
    desc=models.CharField("城市描述",max_length=200)
    create_time=models.DateTimeField("添加时间",auto_now_add=True)

    class Meta:
        verbose_name="城市"
        verbose_name_plural=verbose_name


class CourseOrg(models.Model):
    name=models.CharField("机构名称",max_length=50)
    desc=models.TextField("机构描述")
    click_nums=models.IntegerField("点击数",default=0)
    fav_nums=models.IntegerField("收藏数",default=0)
    image=models.ImageField("封面图",upload_to="org/%Y/%m",max_length=100)
    address=models.CharField("机构地址",max_length=150)
    city=models.ForeignKey(CityDict,"所在城市",on_delete=models.CASCADE)
    create_time=models.DateTimeField("添加时间",auto_now_add=True)

    class Meta:
        verbose_name="课程机构"
        verbose_name_plural=verbose_name

class Teacher(models.Model):
    org=models.ForeignKey(CourseOrg,"所属机构",on_delete=models.CASCADE)
    name=models.CharField("教师名",max_length=50)
    work_years=models.IntegerField("工作年限",default=0)
    work_company=models.CharField("就职公司",max_length=50)
    work_position=models.CharField("公司职位",max_length=50)
    points=models.CharField("教学特点",max_length=50)
    click_nums=models.IntegerField("点击数",default=0)
    fav_nums=models.IntegerField("收藏数",default=0)
    create_time=models.DateTimeField("添加时间",auto_now_add=True)

    class Meta:
        verbose_name="教师"
        verbose_name_plural=verbose_name
