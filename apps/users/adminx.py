import xadmin

from .models import *

from xadmin import views

class BaseSetting(object):
    enable_themes=True
    use_bootswatch=True


class GlobalSettings(object):
    site_title="凉糕后台管理系统"
    site_footer="凉糕在线网"
    menu_style="accordion"


class UserProfilesAdmin(object):
    list_display=['username','nick_name','birday','gender','address','mobile']
    search_fields=['username','nick_name','birday','gender','address','mobile']
    list_filter=['username','nick_name','birday','gender','address','mobile']


class EmailVerifyRecordAdmin(object):
    list_display=['code','email','send_type','send_time']
    search_fields=['coede','email','send_type']
    list_filter=['code','email','send_type','send_time']





class BannerAdmin(object):
    list_display=['title','image','url','index','add_time']
    search_fields=['title','image','url','index']
    list_filter=['title','image','url','index','add_time']


xadmin.site.unregister(UserProfile)
xadmin.site.register(UserProfile,UserProfilesAdmin)
xadmin.site.register(EmailVerifyRecord,EmailVerifyRecordAdmin)
xadmin.site.register(Banner,BannerAdmin)
xadmin.site.register(views.BaseAdminView,BaseSetting)
xadmin.site.register(views.CommAdminView,GlobalSettings)
