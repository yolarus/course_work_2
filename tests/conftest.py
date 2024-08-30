import pytest

from src.vacancy import Vacancy


@pytest.fixture()
def first_vacancy() -> Vacancy:
    return Vacancy("Test",
                   "don't have",
                   "50000 - 100000 - RUR",
                   "description",
                   "requirements",
                   "Москва")


@pytest.fixture()
def second_vacancy() -> Vacancy:
    return Vacancy("Test 2",
                   "don't have",
                   "150000 - 200000 - RUR",
                   "description",
                   "requirements",
                   "Токио")


@pytest.fixture()
def first_vacancy_dict() -> dict:
    return {"name": "Test",
            "url": "don't have",
            "salary": "50000 - 100000 - RUR",
            "short_description": "description",
            "requirements": "requirements",
            "area": "Москва"}
