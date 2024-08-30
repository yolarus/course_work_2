from src.head_hunter_api import HeadHunterAPI
from src.save_to_json_file import SaveToJSONFile
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

    saver_json = SaveToJSONFile()
    saver_json.save_to_file(vacancies[0])
    saver_json.save_to_file(vacancies[0])
    saver_json.add_to_file(vacancies[1])

    data_from_file = saver_json.read_from_file()
    print(data_from_file)
    saver_json.delete_from_file(vacancies[0])
    data_from_file = saver_json.read_from_file()
    print(data_from_file)
