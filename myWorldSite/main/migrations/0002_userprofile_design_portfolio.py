# Generated by Django 4.2.16 on 2025-01-08 13:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="userprofile",
            name="design_portfolio",
            field=models.FileField(blank=True, null=True, upload_to="design_portfolio"),
        ),
    ]
