# Generated by Django 5.1.2 on 2024-10-22 22:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0021_remove_contact_subject'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Contact',
        ),
    ]
