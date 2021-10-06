# Generated by Django 3.2.7 on 2021-10-05 12:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='blogs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('content', models.TextField()),
                ('like', models.BooleanField(default=False)),
                ('dislike', models.BooleanField(default=False)),
            ],
        ),
    ]