# Generated by Django 2.2.7 on 2019-12-10 03:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_user', '0006_auto_20191210_0336'),
    ]

    operations = [
        migrations.AlterField(
            model_name='industry',
            name='industry_type_name',
            field=models.CharField(max_length=25),
        ),
    ]
