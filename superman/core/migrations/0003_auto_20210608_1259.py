# Generated by Django 3.2.4 on 2021-06-08 05:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='company',
            field=models.CharField(default='', max_length=300),
        ),
        migrations.AlterField(
            model_name='email',
            name='email',
            field=models.CharField(default='', max_length=300),
        ),
        migrations.AlterField(
            model_name='profile',
            name='name',
            field=models.CharField(default='', max_length=300),
        ),
    ]
