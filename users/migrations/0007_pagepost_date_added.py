# Generated by Django 4.1.4 on 2023-01-06 08:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_pagepost_author_pagepost_likes'),
    ]

    operations = [
        migrations.AddField(
            model_name='pagepost',
            name='date_added',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]