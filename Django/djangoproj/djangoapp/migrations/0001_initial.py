# Generated by Django 3.2.7 on 2023-05-04 06:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='password',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key', models.CharField(default='', max_length=50, verbose_name='密码键')),
                ('value', models.CharField(default='123456789', max_length=50, verbose_name='密码值')),
                ('desc', models.CharField(default='', max_length=50, verbose_name='描述')),
            ],
        ),
    ]
