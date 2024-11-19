# Generated by Django 5.1.3 on 2024-11-19 21:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth_sys', '0002_customuser_groups_customuser_user_permissions'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='role',
            field=models.CharField(choices=[('student', 'student'), ('teacher', 'teacher')], default='student', max_length=10),
        ),
    ]