from django.urls import path

from .apps import QuizConfig
from .views import QuizListView

app_name = QuizConfig.label

urlpatterns = [
    path("", QuizListView.as_view(), name="index"),
    path("<slug:slug>/", QuizListView.as_view(), name=""),
]
