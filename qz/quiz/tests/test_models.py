from django.test import TestCase
from django.utils import timezone
from django.utils.text import slugify

from .factories import (
    Quiz,
    QuizAnswer,
    QuizAnswerFactory,
    QuizCategory,
    QuizCategoryFactory,
    QuizFactory,
    QuizQuestion,
    QuizQuestionFactory,
)


class QuizCategoryTests(TestCase):
    def setUp(self):
        self.batch_size = 5
        self.test_title = "Quiz Category"

    def test_create(self):
        QuizCategoryFactory.create_batch(self.batch_size)
        self.assertEqual(QuizCategory.objects.count(), self.batch_size)

    def test_update(self):
        quiz_category = QuizCategoryFactory()
        quiz_category.title = "New Title"
        quiz_category.save()
        self.assertEqual(quiz_category.title, "New Title")

    def test_delete(self):
        quiz_category = QuizCategoryFactory()
        quiz_category.delete()
        self.assertEqual(QuizCategory.objects.count(), 0)

    def test_delete_cascade(self):
        quiz_category = QuizCategoryFactory()
        QuizFactory(category=quiz_category)
        quiz_category.delete()
        self.assertEqual(Quiz.objects.count(), 0)

    def test_fields(self):
        quiz_category = QuizCategoryFactory(title=self.test_title)
        quiz_category_1 = QuizCategoryFactory(title=self.test_title)
        # test category 1
        self.assertEqual(quiz_category.title, self.test_title)
        self.assertEqual(quiz_category.slug, slugify(quiz_category.title))
        # test category 2
        self.assertEqual(quiz_category_1.title, self.test_title)
        self.assertEqual(quiz_category_1.slug, slugify(quiz_category.title) + "-1")

    def test_str(self):
        quiz_category = QuizCategoryFactory()
        self.assertEqual(str(quiz_category), quiz_category.title)


class QuizTests(TestCase):
    def setUp(self):
        self.batch_size = 5
        self.test_title = "Quiz"
        self.quiz_category = QuizCategoryFactory()
        self.quiz_category_1 = QuizCategoryFactory()

    def test_create(self):
        QuizFactory.create_batch(self.batch_size)
        self.assertEqual(Quiz.objects.count(), self.batch_size)

    def test_update(self):
        quiz = QuizFactory()
        quiz.title = "New Title"
        quiz.save()
        self.assertEqual(quiz.title, "New Title")
        self.assertEqual(quiz.slug, slugify(quiz.title))

    def test_delete(self):
        quiz = QuizFactory()
        quiz.delete()
        self.assertEqual(Quiz.objects.count(), 0)

    def test_fields(self):
        quiz = QuizFactory(title=self.test_title, category=self.quiz_category)
        quiz_1 = QuizFactory(title=self.test_title, category=self.quiz_category_1)
        # test first quiz
        self.assertEqual(quiz.category, self.quiz_category)
        self.assertEqual(quiz.title, self.test_title)
        self.assertEqual(quiz.slug, slugify(quiz.title))
        self.assertTrue(quiz.description)
        self.assertIn(quiz.status, list(Quiz.Status))
        self.assertIsInstance(quiz.created_at, timezone.datetime)
        self.assertIsInstance(quiz.updated_at, timezone.datetime)
        # test second quiz
        self.assertEqual(quiz_1.category, self.quiz_category_1)
        self.assertEqual(quiz_1.slug, slugify(quiz.title) + "-1")

    def test_str(self):
        quiz = QuizFactory()
        self.assertEqual(str(quiz), quiz.title)


class QuizQuestionTests(TestCase):
    def setUp(self):
        self.batch_size = 5

    def test_create(self):
        QuizQuestionFactory.create_batch(self.batch_size)
        self.assertEqual(QuizQuestion.objects.count(), self.batch_size)


class QuizAnswerTests(TestCase):
    def setUp(self):
        self.batch_size = 5

    def test_create(self):
        QuizAnswerFactory.create_batch(self.batch_size)
        self.assertEqual(QuizAnswer.objects.count(), self.batch_size)
