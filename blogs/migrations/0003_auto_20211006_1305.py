# Generated by Django 3.2.7 on 2021-10-06 07:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0002_blogs_user_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogs',
            name='dislike_count',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='blogs',
            name='like_count',
            field=models.IntegerField(default=0),
        ),
    ]