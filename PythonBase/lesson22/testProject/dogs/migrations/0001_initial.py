# Generated by Django 5.0.4 on 2024-04-08 21:16

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Breed",
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
                ("name", models.CharField(max_length=100)),
                ("description", models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name="Dog",
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
                ("name", models.CharField(max_length=100, verbose_name="Кличка")),
                ("photo", models.ImageField(upload_to="dogs/", verbose_name="Фото")),
                ("birth_date", models.DateField()),
                (
                    "breed",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="dogs.breed"
                    ),
                ),
            ],
        ),
    ]