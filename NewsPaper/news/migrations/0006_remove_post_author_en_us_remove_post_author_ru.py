# Generated by Django 4.0.3 on 2022-05-09 21:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0005_remove_post_creation_date_en_us_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='author_en_us',
        ),
        migrations.RemoveField(
            model_name='post',
            name='author_ru',
        ),
    ]
