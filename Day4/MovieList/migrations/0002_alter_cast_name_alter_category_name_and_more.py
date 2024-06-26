# Generated by Django 5.0.4 on 2024-06-07 13:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MovieList', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cast',
            name='name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='movie',
            name='title',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='series',
            name='title',
            field=models.CharField(max_length=200),
        ),
    ]
