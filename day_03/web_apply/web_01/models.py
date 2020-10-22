from django.db import models

# Create your models here.


class User(models.Model):
    username = models.CharField(max_length=128, verbose_name='用户名')
    password = models.CharField(max_length=128, verbose_name='密码')

    class Meta:
        db_table = 'tb_users'
        verbose_name = '用户表'
