# Generated by Django 2.1.2 on 2019-03-22 21:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('collection', '0006_auto_20190322_1651'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='movie_poster',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]
