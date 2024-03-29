import re
from django import forms

from operation.models import UserAsk


class UserAskForm(forms.ModelForm):
    def clean_mobile(self):
        mobile = self.cleaned_data['mobile']
        REGEX_MOBILE = "^1[358]\d{9}$|^147\d{8}$|^176\d{8}$"
        p = re.compile(REGEX_MOBILE)
        if p.match(mobile):
            return mobile
        else:
            raise forms.ValidationError("手机号格式错误", code="mobile_invalid")

    class Meta:
        model = UserAsk
        fields = ['name', 'mobile', 'course_name']
