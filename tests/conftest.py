import pytest

from src.save_to_json_file import SaveToJSONFile
from src.vacancy import Vacancy


@pytest.fixture()
def first_vacancy() -> Vacancy:
    """
    Фикстура - объект 1 класса Vacancy
    """
    return Vacancy("Test",
                   "don't have",
                   "50000 - 100000 - RUR",
                   "description",
                   "requirements",
                   "Москва")


@pytest.fixture()
def second_vacancy() -> Vacancy:
    """
    Фикстура - объект 2 класса Vacancy
    """
    return Vacancy("Test 2",
                   "don't have",
                   "150000 - 200000 - RUR",
                   "description",
                   "requirements",
                   "Токио")


@pytest.fixture()
def first_vacancy_dict() -> dict:
    """
    Фикстура - объект 1 класса Vacancy, преобразованный в словарь
    """
    return {"name": "Test",
            "url": "don't have",
            "salary": "50000 - 100000 - RUR",
            "short_description": "description",
            "requirements": "requirements",
            "area": "Москва"}


@pytest.fixture()
def second_vacancy_dict() -> dict:
    """
    Фикстура - объект 2 класса Vacancy, преобразованный в словарь
    """
    return {"name": "Test 2",
            "url": "don't have",
            "salary": "150000 - 200000 - RUR",
            "short_description": "description",
            "requirements": "requirements",
            "area": "Можно не рассматривать данную вакансию"}


@pytest.fixture()
def saver_json() -> SaveToJSONFile:
    """
    Фикстура - объект класса SaveToJSONFile
    """
    return SaveToJSONFile("test_data/test")
