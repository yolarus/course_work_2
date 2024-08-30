from src.head_hunter_api import HeadHunterAPI
from src.save_to_json_file import SaveToJSONFile
from src.utils import list_of_vacancies, print_filtered_vacancies


def user_interaction() -> None:
    """
    Функция для взаимодействия с пользователем
    """

    search_query = input("Введите ключевые слова для запроса: ")  # python
    top_n = int(input("Введите количество вакансий (до 100) для вывода в топ N: "))  # 5
    filter_words = input("Введите ключевые слова для фильтрации вакансий: ").lower().split()  # python
    salary_range = input("Введите диапазон зарплат в формате x - y - RUR: ")  # 50000 - 150000 - RUR

    head_hunter_api = HeadHunterAPI()
    full_info_vacancies = head_hunter_api.get_vacancies(search_query)

    vacancies = list_of_vacancies(full_info_vacancies)
    result = print_filtered_vacancies(vacancies, filter_words, salary_range, top_n)

    saver_json = SaveToJSONFile()
    saver_json.clear_file()
    for item in result:
        saver_json.add_to_file(item)
    print("Ваши вакансии выгружены в файл: data/vacancies.json")


if __name__ == "__main__":
    user_interaction()
