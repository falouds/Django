# Generated by Django 2.0 on 2020-03-22 08:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TestModel', '0003_auto_20200322_1548'),
    ]

    operations = [
        migrations.CreateModel(
            name='kddcuptest',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('count', models.IntegerField()),
                ('srv_count', models.IntegerField()),
                ('dst_host_count', models.IntegerField()),
                ('dst_host_srv_sount', models.IntegerField()),
                ('same_srv_rate', models.IntegerField()),
                ('dst_host_same_src_port_rate', models.DecimalField(decimal_places=3, max_digits=8)),
                ('dst_host_serror_rate', models.IntegerField()),
                ('label', models.BooleanField()),
            ],
            options={
                'verbose_name': 'kddcup测试数据集',
                'db_table': 'kddcuptest',
            },
        ),
        migrations.CreateModel(
            name='user',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('user', models.CharField(max_length=20, verbose_name='用户')),
                ('password', models.CharField(max_length=20, verbose_name='密码')),
            ],
            options={
                'verbose_name': '用户',
                'db_table': 'user',
            },
        ),
    ]
