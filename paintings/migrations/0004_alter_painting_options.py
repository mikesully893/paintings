# Generated by Django 4.0.3 on 2022-03-25 17:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('paintings', '0003_painting_image_delete_review'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='painting',
            options={'permissions': [('special_status', 'Purchased a painting')]},
        ),
    ]