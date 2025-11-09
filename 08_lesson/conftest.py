import pytest

from AuthService import AuthService
from ProjectService import ProjectService


@pytest.fixture(scope="session")
def auth_service():
    """Создает экземпляр AuthService для всей сессии."""
    return AuthService()


@pytest.fixture(scope="session")
def auth_token(auth_service):
    """
    Создает ключ авторизации, только если не найдено существующих ключей.
    Использует существующий ключ, если он есть.
    """
    company_id = auth_service.get_company_id()
    existing_keys = auth_service.get_keys_list(company_id)

    if existing_keys:
        first_key_object = existing_keys[0]
        key_value = auth_service.get_key_value(first_key_object)
    else:
        key_value = auth_service.create_key(company_id)
    return key_value


@pytest.fixture
def project_service(auth_token):
    """
    Создает экземпляр ProjectService для каждого теста,
    передавая ему полученный токен.
    """
    return ProjectService(auth_token)


@pytest.fixture(scope="function")
def new_project_id(project_service: ProjectService):
    """
    Создает новый проект перед тестом и возвращает его ID.
    Удаляет проект после завершения теста (Teardown).
    """
    DEFAULT_TITLE = "Автоматизированный Проект"

    project_data = {"title": f"{DEFAULT_TITLE}"}
    response_json = project_service.create_project(project_data)
    project_id = project_service.get_project_id_from_response(response_json)

    yield project_id

    if project_id:
        try:
            project_service.delete_project(project_id)
        except Exception:
            pass


@pytest.fixture
def unauthenticated_project_service():
    """Создает экземпляр ProjectService с пустым токеном для проверки 401/403."""
    return ProjectService(token="")
