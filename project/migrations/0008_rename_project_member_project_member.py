# Generated by Django 5.1.7 on 2025-03-14 05:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0007_project_delete_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='project',
            old_name='project_member',
            new_name='member',
        ),
    ]
