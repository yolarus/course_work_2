from src.base_save_to_file import SaveToFile
from src.vacancy import Vacancy


class SaveToCSVFile(SaveToFile):
    """
    Класс для работы с объектами класса Vacancy и файлом формата .csv
    """
    __file_name: str

    def __init__(self, file_name: str = "vacancies"):
        self.__file_name = file_name

    def save_to_file(self, vacancy: Vacancy) -> None:
        """
        Метод для сохранения объекта класса Vacancy в новый файл формата .csv/ перезаписи файла формата .csv
        """
        pass

    def read_from_file(self) -> None:   # type: ignore[override]
        """
        Метод для получения списка объектов класса Vacancy из файла формата .csv
        """
        pass

    def add_to_file(self, vacancy: Vacancy) -> None:
        """
        Метод для добавления объекта класса Vacancy в файл формата .csv
        """
        pass

    def delete_from_file(self, vacancy: Vacancy) -> None:
        """
        Метод для удаления объекта класса Vacancy из файла формата .csv
        """
        pass
