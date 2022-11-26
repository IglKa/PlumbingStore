# Generated by Django 4.1.3 on 2022-11-26 17:40

import autoslug.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('marketapp', '0004_alter_advertisment_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='advertisment',
            name='category',
            field=models.CharField(choices=[('GOODS', 'Товары'), ('SERVICES', 'Услуги'), ('VACANCY', 'Вакансия')], default='GOODS', max_length=40),
        ),
        migrations.AlterField(
            model_name='advertisment',
            name='slug',
            field=autoslug.fields.AutoSlugField(editable=False, max_length=100, populate_from='title', unique_with=('title', 'date_posted'), verbose_name='URL'),
        ),
    ]
