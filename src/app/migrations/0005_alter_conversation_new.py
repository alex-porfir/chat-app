# Generated by Django 5.0.6 on 2024-07-07 16:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_rename_active_conversation_new'),
    ]

    operations = [
        migrations.AlterField(
            model_name='conversation',
            name='new',
            field=models.BooleanField(blank=True, default=True),
        ),
    ]
