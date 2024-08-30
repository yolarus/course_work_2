import pytest

from src.vacancy import Vacancy


@pytest.fixture
def first_vacancy() -> Vacancy:
    return Vacancy("Test",
                   "don't have",
                   "50000 - 100000 - RUR",
                   "description",
                   "requirements",
                   "Москва")
