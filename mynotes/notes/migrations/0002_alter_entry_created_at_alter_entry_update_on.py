# Generated by Django 4.1 on 2022-08-27 18:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("notes", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="entry",
            name="created_at",
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name="entry",
            name="update_on",
            field=models.DateTimeField(auto_now=True),
        ),
    ]
