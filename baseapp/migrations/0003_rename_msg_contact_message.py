# Generated by Django 4.2.2 on 2023-07-28 18:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('baseapp', '0002_contact'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='msg',
            new_name='message',
        ),
    ]
