# Generated by Django 4.1.7 on 2023-04-03 09:38

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("todo", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="task",
            options={"ordering": ["completed", "created_at"]},
        ),
    ]
