from django.db import models


# Create your models here.


class Category(models.Model):
    """
    文章分类
    """
    title = models.CharField(max_length=20, verbose_name='文章名字')
    position = models.IntegerField(default=1, verbose_name='文章位置')  # 用来排序
    is_show = models.BooleanField(default=True, verbose_name='是否展示文章')  # 用于是否展示
    is_deleted = models.BooleanField(verbose_name='是否删除', null=False)
    create_time = models.DateTimeField(verbose_name='创建时间', auto_now_add=True)
    update_time = models.DateTimeField(verbose_name='更新时间', auto_now=True)

    def __str__(self):
        return self.title


class Article(models.Model):
    """
    文章
    """
    title = models.CharField(max_length=100, verbose_name='文章标题')
    content = models.TextField(max_length=5000, verbose_name='文章类容')
    category = models.ForeignKey(to=Category, on_delete=models.CASCADE)  # 一对多 必须写在多的里面
    # positive_feedback = models.CharField(max_length=10000, )

    def __str__(self):
        return self.title
