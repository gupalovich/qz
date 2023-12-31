# Generated by Django 4.1.9 on 2023-06-30 08:16

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):
    dependencies = [
        ("quiz", "0004_quiz_slug_quiz_status_quizcategory_slug_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="quiz",
            name="created_at",
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="quiz",
            name="updated_at",
            field=models.DateTimeField(auto_now=True),
        ),
    ]
