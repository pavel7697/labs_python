# Generated by Django 2.0 on 2018-01-16 23:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('labapp', '0006_teacher_img'),
    ]

    operations = [
        migrations.AddField(
            model_name='teacher',
            name='description',
            field=models.CharField(default='Нет описания', max_length=1000),
            preserve_default=False,
        ),
    ]
