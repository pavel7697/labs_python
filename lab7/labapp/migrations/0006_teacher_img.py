# Generated by Django 2.0 on 2018-01-16 20:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('labapp', '0005_remove_teacher_img'),
    ]

    operations = [
        migrations.AddField(
            model_name='teacher',
            name='img',
            field=models.FileField(default='/images/def.jpg', upload_to='images'),
            preserve_default=False,
        ),
    ]
