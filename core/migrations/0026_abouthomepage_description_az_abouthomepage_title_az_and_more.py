# Generated by Django 5.1.2 on 2024-10-24 22:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0025_remove_abouthomepage_description_az_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='abouthomepage',
            name='description_az',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='abouthomepage',
            name='title_az',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='aboutus',
            name='description_1_az',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='aboutus',
            name='description_2_az',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='aboutus',
            name='title_1_az',
            field=models.CharField(max_length=120, null=True),
        ),
        migrations.AddField(
            model_name='aboutus',
            name='title_2_az',
            field=models.CharField(max_length=120, null=True),
        ),
        migrations.AddField(
            model_name='producthomepage',
            name='description_az',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='producthomepage',
            name='title_az',
            field=models.CharField(max_length=120, null=True),
        ),
        migrations.AddField(
            model_name='projecthomepage',
            name='title_az',
            field=models.CharField(max_length=120, null=True),
        ),
        migrations.AddField(
            model_name='statistic',
            name='description_az',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
