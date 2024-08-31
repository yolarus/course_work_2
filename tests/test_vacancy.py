from src.vacancy import Vacancy


def test_vacancy_str(first_vacancy: Vacancy) -> None:
    """
    Тест пользовательского отображения для класса Vacancy
    """
    assert str(first_vacancy) == ("Test -- don't have -- 50000 - 100000 - RUR\n"
                                  " -- description\n -- requirements\n -- Москва\n")


def test_vacancy__eq__(first_vacancy: Vacancy, second_vacancy: Vacancy) -> None:
    """
    Тест метода равества для класса Vacancy
    """
    assert (first_vacancy == first_vacancy) is True
    assert (first_vacancy == second_vacancy) is False


def test_vacancy__lt__le__(first_vacancy: Vacancy, second_vacancy: Vacancy) -> None:
    """
    Тест методов меньше и меньше или равно для класса Vacancy
    """
    assert (first_vacancy < second_vacancy) is True
    assert (first_vacancy > second_vacancy) is False
    assert (first_vacancy <= second_vacancy) is True
    assert (first_vacancy >= second_vacancy) is False


def test_vacancy__check_city(first_vacancy: Vacancy, second_vacancy: Vacancy) -> None:
    """
    Тест вальдации места работы для класса Vacancy
    """
    assert first_vacancy.area == "Москва"
    assert second_vacancy.area == "Можно не рассматривать данную вакансию"


def test_vacancy_to_dict(first_vacancy: Vacancy, first_vacancy_dict: dict) -> None:
    """
    Тест преобразования в словарь для класса Vacancy
    """
    assert first_vacancy.to_dict() == first_vacancy_dict
