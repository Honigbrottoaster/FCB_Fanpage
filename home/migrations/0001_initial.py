# Generated by Django 5.0.6 on 2024-05-10 20:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ReviewEntery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('headline', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=1100)),
                ('date', models.DateField()),
            ],
        ),
    ]