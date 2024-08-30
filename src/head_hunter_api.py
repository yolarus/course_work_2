import requests

from src.base_api import BaseAPI


class HeadHunterAPI(BaseAPI):
    """
    Класс для получения вакансий с headhunter.ru
    """
    __url: str
    __vacancies_list: list
    __connection: bool

    @property
    def get_status(self) -> bool:  # type: ignore[override]
        """
        Проверка подключения к headhunter.ru
        """
        if requests.get("https://api.hh.ru/vacancies").status_code == 200:
            self.__connection = True
        else:
            self.__connection = False
        return self.__connection

    def get_vacancies(self, query: str, per_page: int = 100) -> list:
        """
        Возвращает список вакансий по ключевому слову
        """
        if self.get_status:
            self.__url = f"https://api.hh.ru/vacancies?text={query}&per_page={per_page}&only_with_salary={True}"
            self.__vacancies_list = requests.get(self.__url).json()["items"]

        return self.__vacancies_list
