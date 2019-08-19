from django.urls import path, re_path, include

from courses.views import CoursesListView

urlpatterns = [
    # 课程机构
    re_path(r'^list/$', CoursesListView.as_view(), name='list'),
    # re_path(r'^home/(?P<org_id>\d+)/$', OrgHomeView.as_view(), name='home'),
]
