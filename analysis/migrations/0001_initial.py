# New Inital DB Migration Seed 0001

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
                    "submission_type",
                    models.CharField(choices=[("BC", "bytecode")], max_length=100),
                ),
                ("bytecode", models.TextField()),
                ("uuid", models.UUIDField(default=uuid.uuid4, editable=False, unique=True))
                (
                    "result",
                    models.CharField(
                        choices=[
                        ("RECEIVED", "Received"),
                        ("RETRY", "Retry"),
                        ("REVOKED", "Revoked"),
                        ("FAILURE", "Failure"),
                        ("PENDING", "Pending"),
                        ("STARTED", "Started"),
                        ("SUCCESS", "Success"),
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
