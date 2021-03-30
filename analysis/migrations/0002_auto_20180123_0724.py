# 0002_auto_20180123_0724

import uuid

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("analysis", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="analysis", old_name="type", new_name="submission_type",
        ),
        migrations.AddField(
            model_name="analysis",
            name="uuid",
            field=models.UUIDField(default=uuid.uuid4, editable=False, unique=True),
        ),
    ]
