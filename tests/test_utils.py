from typing import Any

from src.utils import list_of_vacancies, print_filtered_vacancies
from src.vacancy import Vacancy


def test_list_of_vacancies(full_info_first_vacancy_dict: dict,
                           full_info_second_vacancy_dict: dict,
                           first_vacancy: Vacancy,
                           second_vacancy: Vacancy) -> None:
    """
    Тестирование функции преобразования списока вакансий из hh.ru в список объектов Vacancy
    """
    assert list_of_vacancies([full_info_first_vacancy_dict,
                              full_info_second_vacancy_dict]) == [first_vacancy, second_vacancy]


def test_print_filtered_vacancies(first_vacancy: Vacancy, second_vacancy: Vacancy, capsys: Any) -> None:
    """
    Тестирование вывода топа вакансий
    """
    result = print_filtered_vacancies([first_vacancy, second_vacancy],
                                      ["description"], "40000 - 120000 - RUR", 1)
    message = capsys.readouterr()
    assert result == [first_vacancy]
    assert message.out.split("\n")[-2] == "Вывод окончен"


def test_print_filtered_vacancies_not_full_top(first_vacancy: Vacancy, second_vacancy: Vacancy, capsys: Any) -> None:
    """
    Тестирование вывода топа вакансий, в случае когда вакансий меньше заданного значения
    """
    result = print_filtered_vacancies([first_vacancy, second_vacancy],
                                      ["description"], "40000 - 120000 - RUR", 2)
    message = capsys.readouterr()
    assert result == [first_vacancy]
    assert message.out.split("\n")[-2] == "Под ваш запрос подходит лишь 1 вакансий"


def test_print_filtered_vacancies_empty(first_vacancy: Vacancy, second_vacancy: Vacancy, capsys: Any) -> None:
    """
    Тестирование вывода топа вакансий, в случае когда ни одна из вакансий не подходит под запрос
    """
    result = print_filtered_vacancies([first_vacancy, second_vacancy],
                                      ["description"], "3000000 - 3000000 - RUR", 2)
    message = capsys.readouterr()
    assert result == []
    assert message.out.split("\n")[-2] == "По вашему запросу не нашлось ни одной вакансии"
