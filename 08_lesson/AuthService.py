import requests
from config import BASE_URL, CREDS


class AuthService:
    """Сервис для выполнения запросов аутентификации и получения токена."""

    def __init__(self):
        self.base_url = BASE_URL
        self.creds = CREDS
        self.response = None
        self.response_json = None

    def check_response_status(self, expected_status=200):  # по умолчанию-200
        assert self.response.status_code == expected_status, \
            (f"Ожидался статус {expected_status}, "
             f"получен {self.response.status_code}. "
             f"Ответ: {self.response.text}")

    def get_company_id(self):
        self.response = requests.post(self.base_url + '/auth/companies',
                                      json=self.creds)
        self.check_response_status()
        self.response_json = self.response.json()
        return self.response_json["content"][0]["id"]

    def _get_key_payload(self, company_id):
        return {
            "login": self.creds["login"],
            "password": self.creds["password"],
            "companyId": company_id
        }

    def create_key(self, company_id):
        key_payload = self._get_key_payload(company_id)
        self.response = requests.post(self.base_url + '/auth/keys',
                                      json=key_payload)
        self.check_response_status(expected_status=201)
        self.response_json = self.response.json()
        return self.response_json["key"]

    def get_keys_list(self, company_id):
        key_payload = self._get_key_payload(company_id)
        self.response = requests.post(self.base_url + '/auth/keys/get',
                                      json=key_payload)
        self.check_response_status()
        self.response_json = self.response.json()
        return self.response_json

    def get_key_value(self, key_object):
        return key_object['key']

    def delete_key(self, key_value):
        self.response = requests.delete(self.base_url +
                                        f'/auth/keys/{key_value}')
        self.check_response_status()
