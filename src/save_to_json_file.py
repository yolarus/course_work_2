import json
from typing import Any

from src.base_save_to_file import SaveToFile
from src.vacancy import Vacancy


class SaveToJSONFile(SaveToFile):
    """
    Класс для работы с объектами класса Vacancy и файлом формата json
    """
    __file_name: str

    def __init__(self, file_name: str = "vacancies"):
        self.__file_name = file_name

    def save_to_file(self, vacancy: Vacancy) -> None:
        """
        Метод для сохранения объекта класса Vacancy в новый файл формата .json/ перезаписи файла формата .json
        """
        data = [vacancy.to_dict()]
        with open(f"data/{self.__file_name}.json", "w") as file:
            json.dump(data, file, indent=4, ensure_ascii=False)

    def read_from_file(self) -> Any:
        """
        Метод для получения списка объектов класса Vacancy из файла формата .json
        """
        with open(f"data/{self.__file_name}.json", "r") as file:
            data = json.load(file)
        return data

    def add_to_file(self, vacancy: Vacancy) -> None:
        """
        Метод для добавления объекта класса Vacancy в файл формата .json
        """
        data = self.read_from_file()
        if vacancy.to_dict() not in data:
            data.append(vacancy.to_dict())
        with open(f"data/{self.__file_name}.json", "w") as file:
            json.dump(data, file, indent=4, ensure_ascii=False)

    def delete_from_file(self, vacancy: Vacancy) -> None:
        """
        Метод для удаления объекта класса Vacancy из файла формата .json
        """
        data = self.read_from_file()

        for index, item in enumerate(data):
            if item == vacancy.to_dict():
                data.pop(index)

        with open(f"data/{self.__file_name}.json", "w") as file:
            json.dump(data, file, indent=4, ensure_ascii=False)
