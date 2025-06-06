# Generated by Django 5.2.2 on 2025-06-05 06:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Product",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=255)),
                ("price", models.FloatField()),
                ("description", models.TextField()),
                ("category", models.CharField(max_length=100)),
                ("image", models.URLField()),
                ("rating_rate", models.FloatField()),
                ("rating_count", models.IntegerField()),
            ],
        ),
    ]
