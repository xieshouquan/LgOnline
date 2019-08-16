from django.urls import path, re_path, include

from organization.views import OrgView, AddUserAskView

urlpatterns = [
    # 课程机构列表页
    re_path(r'^list/$', OrgView.as_view(), name='list'),
    re_path(r'^add_ask/$', AddUserAskView.as_view(), name='add_ask'),
]
