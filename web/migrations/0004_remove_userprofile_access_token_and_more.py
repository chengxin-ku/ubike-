# Generated by Django 5.0.6 on 2024-06-23 14:53

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("web", "0003_userprofile_email_userprofile_line_id_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="userprofile",
            name="access_token",
        ),
        migrations.RemoveField(
            model_name="userprofile",
            name="bio",
        ),
        migrations.RemoveField(
            model_name="userprofile",
            name="carrier",
        ),
        migrations.RemoveField(
            model_name="userprofile",
            name="is_first_login",
        ),
    ]
