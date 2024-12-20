# Generated by Django 5.1.3 on 2024-11-24 15:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth_sys', '0005_userprofile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='role',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='user',
        ),
        migrations.AlterField(
            model_name='customuser',
            name='role',
            field=models.CharField(choices=[('Student', 'student'), ('Moderator', 'moderator'), ('Administrator', 'administrator')], default='student', max_length=13),
        ),
        migrations.DeleteModel(
            name='Role',
        ),
        migrations.DeleteModel(
            name='UserProfile',
        ),
    ]
