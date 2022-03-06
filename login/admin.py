from django.contrib import admin
from login import models
# Register your models here.


class UserManager(admin.ModelAdmin):
    list_display = ['is_deleted', 'create_time', 'update_time', 'phone', 'name', 'pwd', 'gender']


class HobbyManager(admin.ModelAdmin):
    list_display = ['is_deleted', 'create_time', 'update_time', 'hobby']


admin.site.register(models.User, UserManager)
admin.site.register(models.Hobby, HobbyManager)