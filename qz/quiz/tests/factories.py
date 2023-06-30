from factory import Faker, SubFactory
from factory.django import DjangoModelFactory
from factory.fuzzy import FuzzyChoice

from ..models import Quiz, QuizAnswer, QuizCategory, QuizQuestion


class QuizCategoryFactory(DjangoModelFactory):
    class Meta:
        model = QuizCategory

    title = Faker("word")


class QuizFactory(DjangoModelFactory):
    class Meta:
        model = Quiz

    category = SubFactory(QuizCategoryFactory)

    title = Faker("sentence", nb_words=4)
    description = Faker("paragraph", nb_sentences=4)
    status = FuzzyChoice(list(Quiz.Status))


class QuizQuestionFactory(DjangoModelFactory):
    class Meta:
        model = QuizQuestion

    quiz = SubFactory(QuizFactory)

    question = Faker("sentence", nb_words=6)
    explanation = Faker("paragraph", nb_sentences=4)


class QuizAnswerFactory(DjangoModelFactory):
    class Meta:
        model = QuizAnswer

    question = SubFactory(QuizQuestionFactory)

    answer = Faker("sentence", nb_words=6)
    is_correct = FuzzyChoice([True, False])
