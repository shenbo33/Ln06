from django.db import models
import django.utils.timezone as timezone

# Create your models here.


class User(models.Model):
    """
    用户信息
    """
    id = models.CharField('主键', primary_key=True, max_length=40)
    username = models.CharField('用户名', max_length=40)
    password = models.CharField('密码', max_length=40)
    userType = models.CharField('分类', max_length=2, default='1')

    def __unicode__(self):
        return self.name


class Message(models.Model):
    """
    消息
    """
    id = models.CharField('主键', primary_key=True, max_length=40)
    title = models.CharField('标题', max_length=40)
    intr = models.CharField('简介', max_length=256)
    content = models.CharField('内容', max_length=1024)
    username = models.CharField('用户名', max_length=40)
    created = models.DateTimeField('发布时间', default=timezone.now)

    def __unicode__(self):
        return self.content
