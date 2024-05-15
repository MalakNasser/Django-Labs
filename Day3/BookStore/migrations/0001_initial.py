# Generated by Django 5.0.4 on 2024-05-04 14:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, unique=True, verbose_name='Book Title')),
                ('author', models.CharField(max_length=255, verbose_name='Book Author')),
                ('genre', models.CharField(max_length=255, verbose_name='Book Genre')),
                ('publication_year', models.DateField(null=True, verbose_name='Publication Year')),
            ],
        ),
    ]
