# Generated by Django 4.2.16 on 2024-10-27 20:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_group_user_groups_group_permissions'),
    ]

    operations = [
        migrations.RenameField(
            model_name='group_permissions',
            old_name='permission',
            new_name='permissions',
        ),
    ]