# Generated by Django 2.2.4 on 2019-08-16 04:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Launches',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('flight_number', models.IntegerField(default=0)),
                ('launch_date', models.DateField(blank=True, null=True)),
                ('rocket_name', models.CharField(max_length=50)),
                ('mission_patch_link', models.CharField(max_length=200)),
                ('reddit_launch', models.CharField(max_length=200)),
                ('video_link', models.CharField(max_length=200)),
                ('wikipedia', models.CharField(max_length=200)),
                ('article_link', models.CharField(max_length=200)),
                ('details', models.CharField(max_length=500)),
                ('launch_success', models.CharField(max_length=10)),
            ],
        ),
    ]
