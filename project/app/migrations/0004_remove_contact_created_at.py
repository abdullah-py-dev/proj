# Generated by Django 5.1.4 on 2024-12-25 18:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0003_rename_name1_contact_name_contact_created_at"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="contact",
            name="created_at",
        ),
    ]