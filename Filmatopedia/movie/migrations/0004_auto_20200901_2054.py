# Generated by Django 2.1.15 on 2020-09-01 15:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0003_suggestion_req'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='suggestion',
            name='user',
        ),
        migrations.AddField(
            model_name='suggestion',
            name='username',
            field=models.CharField(default='', max_length=100),
        ),
    ]
