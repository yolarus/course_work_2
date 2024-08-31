from src.vacancy import Vacancy


def list_of_vacancies(full_info_vacancies: list) -> list[Vacancy]:
    """
    Функция фозвращает преобразованный список вакансий из hh.ru в список объектов Vacancy
    """
    result = []
    for item in full_info_vacancies:
        result.append(Vacancy(item["name"],
                              item["url"],
                              f'{item["salary"]["from"] if item["salary"]["from"] else item["salary"]["to"]}'
                              f' - {item["salary"]["to"] if item["salary"]["to"] else item["salary"]["from"]}'
                              f' - {item["salary"]["currency"]}',
                              item["snippet"]["responsibility"],
                              item["snippet"]["requirement"],
                              item["area"]["name"]))
    return result


def print_filtered_vacancies(vacancies: list[Vacancy], filter_words: list, salary: str, top_n: int) -> list[Vacancy]:
    """
    Функция для вывода отфильтрованных по ЗП и ключевым словам объектов класса vacancy из списка
    """
    salary_range = [int(i) if i.isdigit() else i for i in salary.split(" - ")]
    flag = 0
    result = []
    for item in vacancies:
        if any(word in str(item.short_description).lower() for word in filter_words):
            item_salary = [int(i) if i.isdigit() else i for i in item.salary.split(" - ")]
            if (salary_range[0] <= item_salary[0] and salary_range[1] >= item_salary[1]  # type: ignore[operator]
                    and salary_range[2] == item_salary[2]):
                flag += 1
                result.append(item)
                print(item)

        if flag == top_n:
            print("Вывод окончен")
            break
    else:
        print("Вывод окончен")
        if flag == 0:
            print("По вашему запросу не нашлось ни одной вакансии")
        elif flag < top_n:
            print(f"Под ваш запрос подходит лишь {flag} вакансий")
    return result
