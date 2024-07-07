from django.db import migrations


GROUP_NAME: str = "Customer Service"


def create_customer_service_group(apps, schema_editor):
    Group = apps.get_model("auth", "Group")

    db_alias = schema_editor.connection.alias
    group, created = Group.objects.using(db_alias).get_or_create(
        name=GROUP_NAME,
        defaults={
            "name": GROUP_NAME,
        },
    )


def delete_customer_service_group(apps, schema_editor):
    Group = apps.get_model("auth", "Group")

    db_alias = schema_editor.connection.alias
    Group.objects.using(db_alias).filter(name=GROUP_NAME).delete()


class Migration(migrations.Migration):
    dependencies = [
        ("authentication", "0001_initial"),
    ]

    operations = [
        migrations.RunPython(
            create_customer_service_group, delete_customer_service_group
        )
    ]
