from src.head_hunter_api import HeadHunterAPI
from src.vacancy import Vacancy

if __name__ == "__main__":

    head_hunter_api = HeadHunterAPI()

    full_vacancies = head_hunter_api.get_vacancies("python", 5)

    print(full_vacancies)
    print(len(full_vacancies))
    print()

    vacancies = []

    for item in full_vacancies:
        vacancies.append(Vacancy(item["name"],
                                 item["url"],
                                 f'{item["salary"]["from"] if item["salary"]["from"] else item["salary"]["to"]}'
                                 f' - {item["salary"]["to"] if item["salary"]["to"] else item["salary"]["from"]}'
                                 f' - {item["salary"]["currency"]}',
                                 item["snippet"]["responsibility"],
                                 item["snippet"]["requirement"],
                                 item["area"]["name"]))

    for item in vacancies:
        print(item.name)
        print(item.url)
        print(item.salary)
        print(item.short_description)
        print(item.requirements)
        print(item.area)
        print()

    print(vacancies[0] == vacancies[1])
    print(vacancies[0] == vacancies[0])
    print(vacancies[2] != vacancies[3])
    print(vacancies[2] > vacancies[3])
    print(vacancies[2] >= vacancies[3])
    print(vacancies[2] < vacancies[3])
    print(vacancies[2] <= vacancies[3])
