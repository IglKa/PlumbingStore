# Generated by Django 4.1.3 on 2022-11-16 18:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('marketapp', '0002_rename_header_advertisment_title_advertisment_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='advertisment',
            name='slug',
            field=models.SlugField(max_length=100, null=True, unique=True, verbose_name='URL'),
        ),
    ]