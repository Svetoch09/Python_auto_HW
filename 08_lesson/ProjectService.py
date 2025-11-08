import requests
from config import BASE_URL


class ProjectService:

    def __init__(self, token):
        self.base_url = BASE_URL
        self.token = token
        self.response = None
        self.response_json = None

        self.headers = {
            "Authorization": f"Bearer {self.token}",
            "Accept": "application/json"
        }

    def get_projects_list(self):
        self.response = requests.get(self.base_url + '/projects', headers=self.headers)
        self.response_json = self.response.json()
        return self.response_json

    def create_project(self, project_data):
        self.response = requests.post(self.base_url + '/projects', headers=self.headers, json=project_data)
        self.response_json = self.response.json()
        return self.response_json

    def update_project(self, project_id, project_data):
        self.response = requests.put(self.base_url + f'/projects/{project_id}', headers=self.headers, json=project_data)
        self.response_json = self.response.json()
        return self.response_json

    def delete_project(self, project_id, project_data={"deleted": True}):
        self.response = requests.put(self.base_url + f'/projects/{project_id}', headers=self.headers, json=project_data)
        self.response_json = self.response.json()
        return self.response_json

    def get_project_id_from_response(self, response_json):
        return response_json.get('id')

    def get_project_by_id(self, project_id):
        self.response = requests.get(self.base_url + f'/projects/{project_id}', headers=self.headers)
        self.response_json = self.response.json()
        return self.response_json

    def check_response_status(self, expected_status=200):
        """Проверяет статус ответа."""
        assert self.response.status_code == expected_status, \
            (f"Ожидался статус {expected_status}, получен {self.response.status_code}. "
             f"Ответ: {self.response.text}")

    def check_project_title(self, expected_title):
        actual_title = self.response_json.get("title")
        assert actual_title == expected_title, \
            (f"Ожидался title {expected_title}, получен {actual_title}. "
             f"Ответ: {self.response.text}")

    def check_project_id(self, expected_project_id):
        actual_project_id = self.response_json.get("id")
        assert actual_project_id == expected_project_id, \
            (f"Ожидался id {expected_project_id}, получен {actual_project_id}. "
             f"Ответ: {self.response.text}")

    def check_response_schema(self, expected_fields =('deleted', 'id', 'title')):
        response_data = self.response_json

        # 1. Проверка наличия всех ожидаемых полей
        for field in expected_fields:
            assert field in response_data, \
                f"Ошибка схемы: Поле '{field}' отсутствует в ответе."

        if 'id' in response_data:
            assert isinstance(response_data['id'], str), \
                f"Ошибка схемы: 'id' должен быть строкой, получен {type(response_data['id'])}"

        if 'title' in response_data:
            assert isinstance(response_data['title'], str), \
                f"Ошибка схемы: 'title' должен быть строкой, получен {type(response_data['title'])}"
