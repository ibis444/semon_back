# Generated by Django 5.1.2 on 2024-10-22 19:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_alter_producthomepage_title'),
    ]

    operations = [
        migrations.CreateModel(
            name='Statistic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='statistics/')),
                ('count', models.IntegerField()),
                ('description', models.CharField(max_length=100)),
            ],
        ),
    ]
