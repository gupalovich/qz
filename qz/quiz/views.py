from django.views.generic import ListView

from .models import QuizCategory


class QuizListView(ListView):
    model = QuizCategory
    template_name = "quiz/list.html"
    context_object_name = "categories"

    def get_queryset(self):
        return super().get_queryset().prefetch_related("quizzes")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
