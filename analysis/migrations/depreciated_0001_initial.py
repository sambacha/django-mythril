# migration 0001

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Analysis",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created", models.DateTimeField(auto_now_add=True)),
                (
                    "type",
                    models.CharField(choices=[("BC", "bytecode")], max_length=100),
                ),
                ("bytecode", models.TextField()),
                (
                    "result",
                    models.CharField(
                        choices=[
                            ("Q", "Queued"),
                            ("I", "In Progress"),
                            ("F", "Finished"),
                            ("E", "Error"),
                        ],
                        max_length=100,
                    ),
                ),
                ("error", models.TextField()),
                ("issues", models.TextField()),
            ],
            options={"ordering": ("created",),},
        ),
    ]
