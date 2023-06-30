from uuid import uuid4

from django.db import models
from model_utils import FieldTracker

from qz.core.utils import slugify_unique


class QuizCategory(models.Model):
    class Meta:
        verbose_name_plural = "Quiz categories"
        indexes = [
            models.Index(fields=["slug"]),
        ]

    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)
    tracker = FieldTracker(fields=["title"])

    def __str__(self):
        return str(self.title)

    def save(self, *args, **kwargs):
        if not self.slug or self.title != self.tracker.previous("title"):
            self.slug = slugify_unique(QuizCategory, self.title)
        return super().save(*args, **kwargs)


class Quiz(models.Model):
    class Meta:
        verbose_name_plural = "Quizzes"
        ordering = ["category__id"]
        indexes = [
            models.Index(fields=["slug"]),
        ]

    class Status(models.TextChoices):
        DRAFT = "DRAFT"
        PUBLISHED = "PUBLISHED"

    category = models.ForeignKey(QuizCategory, related_name="quizzes", on_delete=models.CASCADE)

    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)
    description = models.TextField(blank=True)
    status = models.CharField(max_length=10, choices=Status.choices, default=Status.DRAFT)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    tracker = FieldTracker(fields=["title"])

    def __str__(self):
        return str(self.title)

    def save(self, *args, **kwargs):
        if not self.slug or self.title != self.tracker.previous("title"):
            self.slug = slugify_unique(Quiz, self.title)
        return super().save(*args, **kwargs)


class QuizQuestion(models.Model):
    class Meta:
        verbose_name_plural = "Quiz questions"
        ordering = ["quiz__id"]
        indexes = [
            models.Index(fields=["uuid"]),
        ]

    quiz = models.ForeignKey(Quiz, related_name="questions", on_delete=models.CASCADE)

    uuid = models.UUIDField(default=uuid4, editable=False)
    question = models.TextField()
    explanation = models.TextField(blank=True)

    def __str__(self):
        return str(self.question)


class QuizAnswer(models.Model):
    class Meta:
        verbose_name_plural = "Quiz answers"
        ordering = ["question__id"]

    question = models.ForeignKey(QuizQuestion, related_name="answers", on_delete=models.CASCADE)

    answer = models.TextField()
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return str(self.answer)
