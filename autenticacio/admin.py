from django.contrib import admin
from .models import Curs,Group,
from django.contrib import admin
from allauth.socialaccount.models import SocialAccount, SocialToken
from allauth.account.models import EmailAddress


admin.site.register(Curs)
admin.site.register(Group)

admin.site.unregister(SocialToken)
admin.site.unregister(SocialAccount)

if admin.site.is_registered(EmailAddress):
    admin.site.unregister(EmailAddress)