from src.vacancy import Vacancy


def test_vacancy_str(first_vacancy: Vacancy) -> None:
    assert str(first_vacancy) == "Test -- don't have -- 50000 - 100000 - RUR -- description -- requirements -- Москва"


def test_vacancy__eq__(first_vacancy: Vacancy, second_vacancy: Vacancy) -> None:
    assert (first_vacancy == first_vacancy) is True
    assert (first_vacancy == second_vacancy) is False


def test_vacancy__lt__le__(first_vacancy: Vacancy, second_vacancy: Vacancy) -> None:
    assert (first_vacancy < second_vacancy) is True
    assert (first_vacancy > second_vacancy) is False
    assert (first_vacancy <= second_vacancy) is True
    assert (first_vacancy >= second_vacancy) is False


def test_vacancy__check_city(first_vacancy: Vacancy, second_vacancy: Vacancy) -> None:
    assert first_vacancy.area == "Москва"
    assert second_vacancy.area == "Можно не рассматривать данную вакансию"


def test_vacancy_to_dict(first_vacancy: Vacancy, first_vacancy_dict: dict) -> None:
    assert first_vacancy.to_dict() == first_vacancy_dict
