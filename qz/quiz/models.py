from django.db import models


class Quiz(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)


class QuizCategory(models.Model):
    title = models.CharField(max_length=255)


class QuizQuestion(models.Model):
    quiz = models.ForeignKey(Quiz, related_name="questions", on_delete=models.CASCADE)

    question = models.TextField()


class QuizAnswer(models.Model):
    question = models.ForeignKey(QuizQuestion, related_name="answers", on_delete=models.CASCADE)

    answer = models.TextField()
    is_correct = models.BooleanField(default=False)
