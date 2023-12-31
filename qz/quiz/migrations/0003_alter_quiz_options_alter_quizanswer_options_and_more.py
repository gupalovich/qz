# Generated by Django 4.1.9 on 2023-06-22 13:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("quiz", "0002_quiz_category"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="quiz",
            options={"ordering": ["category__id"], "verbose_name_plural": "Quizzes"},
        ),
        migrations.AlterModelOptions(
            name="quizanswer",
            options={"ordering": ["question__id"], "verbose_name_plural": "Quiz answers"},
        ),
        migrations.AlterModelOptions(
            name="quizcategory",
            options={"verbose_name_plural": "Quiz categories"},
        ),
        migrations.AlterModelOptions(
            name="quizquestion",
            options={"ordering": ["quiz__id"], "verbose_name_plural": "Quiz questions"},
        ),
        migrations.AlterField(
            model_name="quiz",
            name="category",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, related_name="quizzes", to="quiz.quizcategory"
            ),
        ),
    ]
