# Generated by Django 4.2.1 on 2023-05-29 02:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='StoryInfoDjango',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('characters', models.TextField()),
                ('mainchar', models.CharField(max_length=30)),
                ('place', models.CharField(max_length=30)),
                ('time', models.IntegerField()),
                ('wordCount', models.IntegerField()),
                ('theme', models.CharField(max_length=255)),
                ('audience', models.CharField(max_length=255)),
                ('chapters', models.TextField(null=True)),
                ('chapterCount', models.IntegerField()),
                ('wholeStory', models.TextField()),
            ],
        ),
    ]
