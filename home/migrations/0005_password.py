# Generated by Django 5.0.6 on 2024-05-18 15:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_galerieimage_rename_bild_reviewentery_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='PassWord',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=15)),
            ],
        ),
    ]
