from django.db import models
# models.py
 




class User(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.CharField(max_length=20, verbose_name='用户')
    password = models.CharField(max_length=20, verbose_name='密码')
    class Meta:
        db_table = 'user'
        verbose_name = '用户'

class Document(models.Model):
    id = models.AutoField(primary_key=True)
    dir = models.CharField(max_length=150)
    name = models.CharField(max_length=50)
    class Meta:
        db_table = 'document'
        verbose_name = '文件列表'

class DataDB(models.Model):
    id = models.AutoField(primary_key=True)
    count = models.IntegerField()
    srv_count  = models.IntegerField()
    dst_host_count = models.IntegerField()
    dst_host_srv_count = models.IntegerField()
    same_srv_rate = models.IntegerField()
    dst_host_same_src_port_rate = models.FloatField()
    dst_host_serror_rate = models.IntegerField()
    label = models.IntegerField()
    class Meta:
        db_table = 'data'
        verbose_name = '数据'