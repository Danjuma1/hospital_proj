# Generated by Django 3.2.8 on 2021-10-16 17:42

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
            name='Blogpost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('image', models.ImageField(upload_to='images/BlogImages')),
                ('content', models.TextField(max_length=40000)),
                ('summary', models.CharField(max_length=150)),
                ('category', models.CharField(choices=[('Mental Health', 'Mental Health'), ('Heart Disease', 'Heart Disease'), ('Covid19', 'Covid19'), ('Immunization', 'Immunization')], max_length=50)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
