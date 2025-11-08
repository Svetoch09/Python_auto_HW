import pytest
import requests
from ProjectService import ProjectService

# --- КОНСТАНТЫ ---
DEFAULT_TITLE = "Автоматизированный Проект"
UPDATED_TITLE = "Измененное Название"


# ==============================================================================
#                            ПРОВЕРКИ АВТОРИЗАЦИИ (401)
# ==============================================================================

class TestAuthentication:

    @pytest.mark.negative
    def test_create_without_auth(self,
                                 unauthenticated_project_service:
                                 ProjectService):
        """[POST -] Создание проекта без токена авторизации (ожидаем 401)."""
        project_data = {"title": DEFAULT_TITLE}
        unauthenticated_project_service.create_project(project_data)
        unauthenticated_project_service.check_response_status(
            expected_status=401)

    def test_get_project_without_auth(self,
                                      unauthenticated_project_service:
                                      ProjectService, new_project_id):
        """[GET -] Запрос проекта без токена авторизации (ожидаем 401)."""

        unauthenticated_project_service.get_project_by_id(new_project_id)
        unauthenticated_project_service.check_response_status(
            expected_status=401)

    def test_update_without_auth(self,
                                 unauthenticated_project_service:
                                 ProjectService, new_project_id):
        """Попытка изменить проект без токена авторизации (ожидаем 401)."""
        update_data = {"title": UPDATED_TITLE}
        unauthenticated_project_service.update_project(new_project_id,
                                                       update_data)
        unauthenticated_project_service.check_response_status(
            expected_status=401)


# ==============================================================================
#                   ПРОВЕРКИ БЕЗОПАСНОСТИ МЕТОДОВ (405)
# ==============================================================================

class TestMethodSecurity:
    @pytest.mark.negative
    def test_disallowed_delete_on_creation_endpoint(self,
                                                    project_service:
                                                    ProjectService):
        """DELETE на /projects должен быть отклонен."""
        project_service.response = requests.delete(
            project_service.base_url + '/projects',
            headers=project_service.headers
        )
        project_service.check_response_status(expected_status=404)

    def test_disallowed_patch_on_project_id(self,
                                            project_service:
                                            ProjectService, new_project_id):
        """Метод PATCH на /projects/{id} должен быть отклонен."""
        update_data = {"title": "PATCH Test"}
        project_service.response = requests.patch(
            project_service.base_url + f'/projects/{new_project_id}',
            headers=project_service.headers,
            json=update_data
        )
        project_service.check_response_status(expected_status=404)

        new_project_id = None
