"""
Создать класс для работы с вакансиями. В этом классе самостоятельно определить атрибуты,
такие как название вакансии, ссылка на вакансию, зарплата, краткое описание или требования и т. п.
(всего не менее четырех атрибутов).
Класс должен поддерживать методы сравнения вакансий между собой по зарплате и валидировать данные,
которыми инициализируются его атрибуты.
Способами валидации данных может быть проверка, указана или нет зарплата.
В этом случае выставлять значение зарплаты 0 или «Зарплата не указана» в зависимости от структуры класса.
"""


class Vacancy:
    """
    Класс для работы с вакансиями
    """
    __slots__ = ("name", "url", "salary", "short_description", "requirements", "area")
    name: str
    url: str
    salary: str
    short_description: str
    requirements: str
    area: str

    def __init__(self, name: str, url: str, salary: str, short_description: str, requirements: str, area: str) -> None:
        """
        Конструктор объектов
        """
        self.name = name
        self.url = url
        self.salary = salary
        self.short_description = short_description
        self.requirements = requirements
        self.__check_city(area)

    def __str__(self) -> str:
        return (f"{self.name} -- {self.url} -- {self.salary} -- {self.short_description}"
                f" -- {self.requirements} -- {self.area}")

    def __eq__(self, other: "Vacancy") -> bool:   # type: ignore[override]
        """
        Метод для проверки зарплат вакансий - равно
        """
        if (self.salary.split(" - ")[0] == other.salary.split(" - ")[0]
                and self.salary.split(" - ")[2] == other.salary.split(" - ")[2]):
            return True
        else:
            return False

    def __lt__(self, other: "Vacancy") -> bool:
        """
        Метод для проверки зарплат вакансий - меньше
        """
        if (self.salary.split(" - ")[0] < other.salary.split(" - ")[0]
                and self.salary.split(" - ")[2] == other.salary.split(" - ")[2]):
            return True
        else:
            return False

    def __le__(self, other: "Vacancy") -> bool:
        """
        Метод для проверки зарплат вакансий - меньше или равно
        """
        if (self.salary.split(" - ")[0] <= other.salary.split(" - ")[0]
                and self.salary.split(" - ")[2] == other.salary.split(" - ")[2]):
            return True
        else:
            return False

    def __check_city(self, area: str) -> None:
        """
        Валидация вакансии по месту работы
        """
        if area == "Москва":
            self.area = area
        else:
            self.area = "Можно не рассматривать данную вакансию"

    def to_dict(self) -> dict:
        return {"name": self.name, "url": self.url, "salary": self.salary, "short_description": self.short_description,
                "requirements": self.requirements, "area": self.area}
