# Generated by Django 3.1.1 on 2020-09-15 20:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('MDSite', '0007_auto_20200916_0153'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='body',
            new_name='comm',
        ),
        migrations.RenameField(
            model_name='comment',
            old_name='date_added',
            new_name='time',
        ),
        migrations.RenameField(
            model_name='comment',
            old_name='name',
            new_name='user',
        ),
        migrations.RenameField(
            model_name='subcomment',
            old_name='body',
            new_name='comm',
        ),
        migrations.RenameField(
            model_name='subcomment',
            old_name='date_added',
            new_name='time',
        ),
        migrations.RenameField(
            model_name='subcomment',
            old_name='name',
            new_name='user',
        ),
    ]
