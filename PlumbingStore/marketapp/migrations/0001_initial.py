# Generated by Django 4.1.3 on 2022-12-09 17:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Advertisment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(choices=[('GOODS', 'Товары'), ('SERVICES', 'Услуги'), ('VACANCY', 'Вакансия')], default='GOODS', max_length=15)),
                ('title', models.CharField(max_length=150)),
                ('description', models.TextField(max_length=5000)),
                ('image', models.ImageField(blank=True, upload_to='')),
                ('date_posted', models.DateTimeField(default=django.utils.timezone.now)),
                ('slug', models.SlugField(max_length=100, unique=True, verbose_name='URL')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('descr', models.TextField(max_length=5000)),
                ('header_image', models.ImageField(blank=True, upload_to='')),
                ('profile_image', models.ImageField(blank=True, upload_to='')),
                ('date_created', models.DateTimeField(default=django.utils.timezone.now)),
                ('category', models.CharField(choices=[('SHOP', 'Shop'), ('STARTUP', 'Startup'), ('BUSINESS', 'Business')], default='SHOP', max_length=10)),
                ('slug', models.SlugField(max_length=100, unique=True, verbose_name='URL')),
                ('holder', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(max_length=5000)),
                ('image', models.ImageField(blank=True, upload_to='')),
                ('date_posted', models.DateTimeField(default=django.utils.timezone.now)),
                ('advert', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='marketapp.advertisment')),
                ('company', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='marketapp.company')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
