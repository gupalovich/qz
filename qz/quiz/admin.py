from django.contrib import admin

from .models import Quiz, QuizAnswer, QuizCategory, QuizQuestion


@admin.register(Quiz)
class QuizAdmin(admin.ModelAdmin):
    list_display = ("title", "category")


@admin.register(QuizCategory)
class QuizCategoryAdmin(admin.ModelAdmin):
    list_display = ("title",)


@admin.register(QuizQuestion)
class QuizQuestionAdmin(admin.ModelAdmin):
    list_display = ("quiz", "question")


@admin.register(QuizAnswer)
class QuizAnswerAdmin(admin.ModelAdmin):
    list_display = ("question", "answer")
    list_filter = ("question",)
    search_fields = ("question__question",)
    ordering = ("question",)
