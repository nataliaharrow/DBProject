# Generated by Django 2.2.7 on 2019-12-16 00:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_user', '0019_auto_20191215_1902'),
    ]

    operations = [
        migrations.AddField(
            model_name='userrequest',
            name='reqname',
            field=models.CharField(default='exit', max_length=100),
            preserve_default=False,
        ),
    ]
