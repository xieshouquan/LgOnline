from django.urls import re_path

from organization.views import OrgView, AddUserAskView, OrgHomeView, OrgCourseView, OrgDescView, OrgTeacherView, \
    AddFavView

urlpatterns = [
    # 课程机构
    re_path(r'^list/$', OrgView.as_view(), name='list'),
    re_path(r'^add_ask/$', AddUserAskView.as_view(), name='add_ask'),
    re_path(r'^home/(?P<org_id>\d+)/$', OrgHomeView.as_view(), name='home'),
    re_path(r'^course/(?P<org_id>\d+)/$', OrgCourseView.as_view(), name='course'),
    re_path(r'^desc/(?P<org_id>\d+)/$', OrgDescView.as_view(), name='desc'),
    re_path(r'^teacher/(?P<org_id>\d+)/$', OrgTeacherView.as_view(), name='teacher'),

    # 机构收藏
    re_path(r'^add_fav/$', AddFavView.as_view(), name='add_fav'),
]
