import pytest
from django.db.models import Model
from django.utils.text import slugify
from transliterate import translit

from ..utils import capitalize_slug, capitalize_str, slugify_unique


def model_slug_test_generator(model: Model, test_slug: str, create=5) -> None:
    for i in range(create):
        slug = slugify_unique(model, test_slug)
        obj = model.objects.create(label=test_slug, slug=slug)
        res_slug = f"{slugify(test_slug)}-{i}" if i > 0 else slugify(test_slug)
        assert "@" not in res_slug
        assert obj.slug == res_slug


@pytest.mark.django_db
def test_slugify_unique() -> None:
    """
    Test unique slug generation; conversion to ru locale
    TODO: test
    """
    # cases = [
    #     "some @ long giberish-dsfgsdfg!",
    #     translit("тест @ заголовок!", "ru", reversed=True),  # test-zagolovok
    # ]
    # for slug in cases:
    #     model_slug_test_generator(Tag, slug)


def test_capitalize_str() -> None:
    cases = [
        ("test title", "Test Title"),
        ("test-zagolovok", "Test-zagolovok"),
        ("тест @ заголовок!", "Тест @ Заголовок!"),
    ]
    for case, expected_result in cases:
        func_res = capitalize_str(case)
        assert func_res == expected_result


def test_capitalize_slug() -> None:
    cases = [
        ("test-title", "Test Title"),
        ("test-zagolovok", "Test Zagolovok"),
        ("test-zagolovok-1", "Test Zagolovok"),
    ]
    for case, expected_result in cases:
        func_res = capitalize_slug(case)
        assert func_res == expected_result
