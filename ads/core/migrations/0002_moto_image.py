# Generated by Django 4.2 on 2024-05-28 17:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='moto',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='core/image'),
        ),
    ]
