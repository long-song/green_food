# Generated by Django 2.1.8 on 2019-07-21 12:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Adress',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('aname', models.CharField(max_length=50, verbose_name='收货人')),
                ('ads', models.CharField(max_length=300, verbose_name='地址')),
                ('aphone', models.CharField(max_length=20, verbose_name='电话')),
            ],
        ),
        migrations.CreateModel(
            name='User_order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('orderNo', models.CharField(max_length=50, verbose_name='订单号')),
                ('orderdetail', models.TextField(verbose_name='订单详情')),
                ('adsname', models.CharField(max_length=30, verbose_name='收件人姓名')),
                ('adsphone', models.CharField(max_length=20, verbose_name='收件人电话')),
                ('ads', models.CharField(max_length=300, verbose_name='地址')),
                ('time', models.DateTimeField(auto_now=True, verbose_name='下单时间')),
                ('acot', models.IntegerField(default=1, verbose_name='总数')),
                ('acount', models.DecimalField(decimal_places=2, max_digits=8, verbose_name='订单总价')),
                ('orderstatus', models.IntegerField(choices=[(1, '未支付'), (2, '已支付'), (3, '订单取消')], default=1, verbose_name='订单状态')),
            ],
        ),
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=15, unique=True, verbose_name='用户名')),
                ('password', models.CharField(max_length=256, verbose_name='密码')),
                ('phone', models.CharField(max_length=11, unique=True, verbose_name='手机号')),
                ('head_img', models.ImageField(default='static/images/product_img_17.png', upload_to='static/images', verbose_name='头像')),
                ('t_name', models.CharField(max_length=10, null=True, verbose_name='真实姓名')),
                ('gender', models.IntegerField(choices=[(1, '男'), (2, '女')], default=1, verbose_name='性别')),
                ('email', models.EmailField(max_length=254, null=True, unique=True, verbose_name='邮箱')),
                ('up_time', models.DateTimeField(auto_now_add=True, verbose_name='注册时间')),
                ('allow_order', models.IntegerField(default=0, verbose_name='订单管理权限')),
                ('allow_data', models.IntegerField(default=0, verbose_name='数据管理权限')),
                ('superuser', models.IntegerField(default=0, verbose_name='超级管理员')),
            ],
        ),
        migrations.AddField(
            model_name='user_order',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user_app.UserInfo'),
        ),
        migrations.AddField(
            model_name='adress',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user_app.UserInfo'),
        ),
    ]