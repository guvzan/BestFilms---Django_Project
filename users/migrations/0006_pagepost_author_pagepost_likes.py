# Generated by Django 4.1.4 on 2023-01-06 08:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_pagepost_image_pagepost_text_alter_customuser_dob'),
    ]

    operations = [
        migrations.AddField(
            model_name='pagepost',
            name='author',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='pagepost',
            name='likes',
            field=models.IntegerField(default=0),
        ),
    ]