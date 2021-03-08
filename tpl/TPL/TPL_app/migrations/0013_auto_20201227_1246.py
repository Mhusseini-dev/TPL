# Generated by Django 2.2.4 on 2020-12-27 10:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TPL_app', '0012_auto_20201227_1140'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='child',
            name='gender',
        ),
        migrations.RemoveField(
            model_name='lesson',
            name='max_students',
        ),
        migrations.RemoveField(
            model_name='parent',
            name='is_parent',
        ),
        migrations.RemoveField(
            model_name='teacher',
            name='is_teacher',
        ),
        migrations.AddField(
            model_name='teacher',
            name='gender',
            field=models.CharField(max_length=6, null=True),
        ),
    ]