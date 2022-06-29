# Generated by Django 3.2.13 on 2022-06-22 17:03

from django.db import migrations, models
import uuid

from core.migration_helpers import AddDefaultUUIDs


class Migration(migrations.Migration):

    dependencies = [
        ("slack", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="slackconfiguration",
            name="uuid",
            field=models.UUIDField(default=uuid.uuid4, editable=False, null=True),
        ),
        migrations.RunPython(
            AddDefaultUUIDs("slack", "slackconfiguration"),
            reverse_code=migrations.RunPython.noop,
        ),
        migrations.AlterField(
            model_name="slackconfiguration",
            name="uuid",
            field=models.UUIDField(default=uuid.uuid4, editable=False, unique=True),
        ),
        migrations.AddField(
            model_name="slackenvironment",
            name="uuid",
            field=models.UUIDField(default=uuid.uuid4, editable=False, null=True),
        ),
        migrations.RunPython(
            AddDefaultUUIDs("slack", "slackenvironment"),
            reverse_code=migrations.RunPython.noop,
        ),
        migrations.AlterField(
            model_name="slackenvironment",
            name="uuid",
            field=models.UUIDField(default=uuid.uuid4, editable=False, unique=True),
        ),
    ]
