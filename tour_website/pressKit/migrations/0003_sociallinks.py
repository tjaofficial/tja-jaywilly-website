# Generated by Django 5.0.1 on 2024-03-19 19:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pressKit', '0002_shows_ticket_link'),
    ]

    operations = [
        migrations.CreateModel(
            name='socialLinks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('artistName', models.CharField(max_length=50)),
                ('instagram', models.CharField(max_length=300)),
                ('youtube', models.CharField(max_length=300)),
                ('spotify', models.CharField(max_length=300)),
                ('spotifyURI', models.CharField(max_length=300)),
                ('apple', models.CharField(max_length=300)),
                ('twitterX', models.CharField(max_length=300)),
                ('facebook', models.CharField(max_length=300)),
                ('tiktok', models.CharField(max_length=300)),
                ('snapchat', models.CharField(max_length=300)),
                ('soundcloud', models.CharField(max_length=300)),
            ],
        ),
    ]
