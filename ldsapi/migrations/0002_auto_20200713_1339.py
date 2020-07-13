# Generated by Django 3.0.8 on 2020-07-13 12:39

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('ldsapi', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='hero',
            name='date_created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='hero',
            name='date_modified',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='hero',
            name='alias',
            field=models.CharField(max_length=60, unique=True),
        ),
        migrations.AlterField(
            model_name='hero',
            name='name',
            field=models.CharField(max_length=60, unique=True),
        ),
    ]