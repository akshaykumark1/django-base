# Generated by Django 5.1.4 on 2024-12-19 13:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='gallery_images/')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField(max_length=200)),
            ],
        ),
    ]
