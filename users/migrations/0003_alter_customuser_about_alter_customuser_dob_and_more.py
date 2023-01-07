# Generated by Django 4.1.4 on 2023-01-05 13:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_customuser_post_list'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='about',
            field=models.TextField(blank=True, default='---', null=True),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='dob',
            field=models.DateTimeField(blank=True, default='1999-19-9', null=True),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='status',
            field=models.CharField(default='---', max_length=100),
        ),
    ]
