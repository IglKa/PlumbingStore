# Generated by Django 4.1.3 on 2022-11-14 13:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usersapp', '0003_alter_user_employee_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(blank=True, default=None, max_length=45, null=True),
        ),
    ]