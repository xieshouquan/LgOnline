import xadmin

from .models import *


class CourseAdmin(object):
    list_display = ['name', 'desc', 'detail', 'degree', 'learn_times', 'students', 'fav_nums', 'click_nums']
    search_fields = ['name', 'desc', 'detail', 'degree', 'learn_times', 'students', 'fav_nums', 'click_nums']
    list_filter = ['name', 'desc', 'detail', 'degree', 'learn_times', 'students', 'fav_nums', 'click_nums']


class LessonAdmin(object):
    list_display = ['course', 'name', 'create_time']
    search_fields = ['course', 'name']
    list_filter = ['course', 'name', 'create_time']


class VideoAdmin(object):
    list_display = ['lesson', 'name', 'create_time']
    search_fields = ['lesson', 'name']
    list_filter = ['lesson', 'name', 'create_time']


class CourseResourceAdmin(object):
    list_display = ['course', 'name', 'download', 'create_time']
    search_fields = ['course', 'name', 'download']
    list_filter = ['course', 'name', 'download', 'create_time']


xadmin.site.register(Course, CourseAdmin)
xadmin.site.register(Lesson, LessonAdmin)
xadmin.site.register(Video, VideoAdmin)
xadmin.site.register(CourseResource, CourseResourceAdmin)
