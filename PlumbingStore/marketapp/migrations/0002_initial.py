# Generated by Django 4.1.3 on 2023-01-08 13:16

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('marketapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='follow',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='feedback',
            name='content_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contenttypes.contenttype'),
        ),
        migrations.AddField(
            model_name='feedback',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='company',
            name='category',
            field=models.ForeignKey(help_text="Choose category of your Company. If it's not in the list just write it down and it will be created in our Data Base for future uses", null=True, on_delete=django.db.models.deletion.PROTECT, to='marketapp.companycategory'),
        ),
        migrations.AddField(
            model_name='advertisment',
            name='category',
            field=models.ForeignKey(help_text="Choose category of your Advertisment. If it's not in the list just write it down and it will be created in our Data Base for future uses", null=True, on_delete=django.db.models.deletion.PROTECT, to='marketapp.advertcategory'),
        ),
        migrations.AddField(
            model_name='advertisment',
            name='company',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='marketapp.company', to_field='slug'),
        ),
    ]
