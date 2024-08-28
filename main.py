from src.head_hunter_api import HeadHunterAPI


if __name__ == "__main__":

    head_hunter_api = HeadHunterAPI()

    vacancies = head_hunter_api.get_vacancies("python", 25)

    print(vacancies)
    print(len(vacancies))
