# Generated by Django 5.0.3 on 2024-03-09 20:12

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("boards", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="board",
            name="writer",
            field=models.CharField(default=2, max_length=30),
            preserve_default=False,
        ),
    ]