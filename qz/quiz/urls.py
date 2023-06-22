from django.urls import path

from .apps import QuizConfig
from .views import QuizListView

app_name = QuizConfig.label

urlpatterns = [
    path("", QuizListView.as_view(), name="quiz_list"),
]
