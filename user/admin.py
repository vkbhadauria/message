from django.contrib import admin
from .models import User, Group, GroupUser
from django.contrib.auth.models import Group as GroupPermission
# Register your models here.

admin.site.register(User)
admin.site.register(Group)
admin.site.register(GroupUser)
admin.site.unregister(GroupPermission)
