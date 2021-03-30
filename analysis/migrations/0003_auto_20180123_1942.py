# 0003_auto_20180123_1942

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("analysis", "0002_auto_20180123_0724"),
    ]

    operations = [
        migrations.AlterField(
            model_name="analysis",
            name="result",
            field=models.CharField(
                blank=True,
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
        migrations.AlterField(
            model_name="analysis",
            name="submission_type",
            field=models.CharField(choices=[("bytecode", "bytecode")], max_length=100),
        ),
    ]
