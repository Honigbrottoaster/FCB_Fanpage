# Generated by Django 5.0.6 on 2024-05-11 17:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_reviewentery_bild'),
    ]

    operations = [
        migrations.CreateModel(
            name='GalerieImage',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('image', models.ImageField(upload_to='')),
            ],
        ),
        migrations.RenameField(
            model_name='reviewentery',
            old_name='bild',
            new_name='image',
        ),
    ]
