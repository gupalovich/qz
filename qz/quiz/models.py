from django.db import models


class QuizCategory(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return str(self.title)

    class Meta:
        verbose_name_plural = "Quiz categories"


class Quiz(models.Model):
    category = models.ForeignKey(QuizCategory, related_name="quizzes", on_delete=models.CASCADE)

    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)

    def __str__(self):
        return str(self.title)

    class Meta:
        verbose_name_plural = "Quizzes"
        ordering = ["category__id"]


class QuizQuestion(models.Model):
    quiz = models.ForeignKey(Quiz, related_name="questions", on_delete=models.CASCADE)

    question = models.TextField()

    def __str__(self):
        return str(self.question)

    class Meta:
        verbose_name_plural = "Quiz questions"
        ordering = ["quiz__id"]


class QuizAnswer(models.Model):
    question = models.ForeignKey(QuizQuestion, related_name="answers", on_delete=models.CASCADE)

    answer = models.TextField()
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return str(self.answer)

    class Meta:
        verbose_name_plural = "Quiz answers"
        ordering = ["question__id"]
