# Generated by Django 3.2.4 on 2021-07-01 07:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('countries', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='countries',
            options={},
        ),
        migrations.AlterField(
            model_name='countries',
            name='capital',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='countries',
            name='name',
            field=models.TextField(),
        ),
    ]
