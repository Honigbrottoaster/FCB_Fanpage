# Generated by Django 5.0.6 on 2024-05-11 17:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_alter_reviewentery_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='reviewentery',
            name='bild',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]