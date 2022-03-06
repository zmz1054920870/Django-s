from django.db import models


# Create your models here.


class BaseUser(models.Model):
    is_deleted = models.BooleanField(verbose_name='是否删除', null=False)
    create_time = models.DateTimeField(verbose_name='创建时间', auto_now_add=True)
    update_time = models.DateTimeField(verbose_name='更新时间', auto_now=True)
    test_one = models.CharField(verbose_name='测试null', null=True, max_length=20)
    test_two = models.CharField(verbose_name='测试blank', blank=True, max_length=20)
    test_three = models.CharField(verbose_name='测试null+blank', blank=True, null=True, max_length=20)

    class Meta:
        abstract = True


class Hobby(models.Model):
    """
    爱好表
    """
    is_deleted = models.BooleanField(verbose_name='是否删除', null=False)
    create_time = models.DateTimeField(verbose_name='创建时间', auto_now_add=True)
    update_time = models.DateTimeField(verbose_name='更新时间', auto_now=True)
    hobby_list = {
        ('0', '抽烟'),
        ('1', '喝酒'),
        ('2', '烫头')
    }
    hobby = models.CharField(verbose_name='爱好', choices=hobby_list, null=False, max_length=20)

    def __str__(self):
        return self.hobby


class User(BaseUser):
    """
    用户表
    """
    phone = models.CharField(verbose_name='电话', max_length=11, null=False)
    name = models.CharField(verbose_name='用户', max_length=20, null=False)
    pwd = models.CharField(verbose_name='密码', max_length=64, null=False)
    gender = models.CharField(verbose_name='性别', max_length=3, null=False)
    hb = models.ManyToManyField(to=Hobby)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '用户表'
        verbose_name_plural = verbose_name
        db_table = 'user'
