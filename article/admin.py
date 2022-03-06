from django.contrib import admin
from .models import *
# Register your models here.


class CategoryManager(admin.ModelAdmin):
    list_display = [
        'title',
        'position',
        'is_show',
        'is_deleted',
        'create_time',
        'update_time'
    ]


class ArticleManager(admin.ModelAdmin):
    list_display = [
        'title',
        'content',
        'category'
    ]


admin.site.register(Category, CategoryManager)
admin.site.register(Article, ArticleManager)