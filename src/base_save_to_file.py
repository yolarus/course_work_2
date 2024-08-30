from abc import ABC, abstractmethod
from typing import Any

from src.vacancy import Vacancy


class SaveToFile(ABC):
    """
    Абстрактный класс для работы с объектами класса Vacancy и файломи различного формата
    """
    @abstractmethod
    def save_to_file(self, vacancy: Vacancy) -> None:
        """
        Абстрактный метод для сохранения объекта класса Vacancy в новый файл/ перезаписи файла
        """
        pass

    @abstractmethod
    def read_from_file(self) -> Any:
        """
        Абстрактный метод для получения списка объектов класса Vacancy из файла
        """
        pass

    @abstractmethod
    def add_to_file(self, vacancy: Vacancy) -> None:
        """
        Абстрактный метод для добавления объекта класса Vacancy в файл
        """
        pass

    @abstractmethod
    def delete_from_file(self, vacancy: Vacancy) -> None:
        """
        Абстрактный метод для удаления объекта класса Vacancy из файла
        """
        pass
