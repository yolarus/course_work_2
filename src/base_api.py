from abc import ABC, abstractmethod


class BaseAPI(ABC):
    """
    Абстрактный класс для работы с API поиска вакансий
    """

    @abstractmethod
    def get_status(self) -> bool:
        """
        Проверка подключения к API
        """
        pass

    @abstractmethod
    def get_vacancies(self, query: str) -> list:
        """
        Возвращает список вакансий по поисковому запросу
        """
        pass
