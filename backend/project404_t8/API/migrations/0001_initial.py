# Generated by Django 2.1.5 on 2019-03-14 18:08

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('datetime', models.DateTimeField(blank=True, default=datetime.datetime.now)),
            ],
        ),
        migrations.CreateModel(
            name='Follow',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Friendship',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=250)),
                ('body', models.TextField()),
                ('image_link', models.FileField(blank=True, null=True, upload_to='')),
                ('privacy_setting', models.CharField(choices=[('1', 'me'), ('2', 'another author'), ('3', 'my friends'), ('4', 'friends of friends'), ('5', 'only friends on my host'), ('6', 'public')], default='1', max_length=1)),
                ('is_markdown', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Server',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
            ],
        ),
    ]
