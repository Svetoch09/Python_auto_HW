import pytest
from ProjectService import ProjectService

# --- КОНСТАНТЫ ---
DEFAULT_TITLE = "Автоматизированный Проект"
UPDATED_TITLE = "Измененное Название"

# ==============================================================================
#                                CRUD (ПОЗИТИВ)
# ==============================================================================

class TestPositiveCRUD:
    @pytest.mark.positive
    def test_create_and_get_project(self, project_service: ProjectService, new_project_id):
        project_service.get_project_by_id(new_project_id)
        project_service.check_response_status()
        project_service.check_project_id(new_project_id)
        project_service.check_project_title(DEFAULT_TITLE)

    def test_update_project_title(self, project_service: ProjectService, new_project_id):
        update_data = {"title": UPDATED_TITLE}
        project_service.update_project(new_project_id, update_data)
        project_service.check_response_status()
        project_service.get_project_by_id(new_project_id)
        project_service.check_project_title(UPDATED_TITLE)
        project_service.get_project_by_id(new_project_id)

    def test_delete_project(self, project_service: ProjectService, new_project_id):
        project_service.delete_project(new_project_id)
        project_service.check_response_status()
        project_service.get_project_by_id(new_project_id)
        project_service.check_response_status()
        assert project_service.response_json.get("deleted") is True, \
         f"Ожидалось, что поле 'deleted' будет true после удаления."

        # Очищаем ID фикстуры - не пытаться удалить его в TEARDOWN
        new_project_id = None

# ==============================================================================
#                      ПРОВЕРКИ СХЕМЫ (SCHEMA VALIDATION)
# ==============================================================================

class TestSchemaValidation:
    @pytest.mark.positive
    def test_schema_after_creation(self, project_service: ProjectService):
        """Проверка схемы JSON после успешного POST-запроса."""
        project_data = {"title": "Проект для проверки схемы"}
        project_service.create_project(project_data)
        project_service.check_response_schema(expected_fields=('id',)) #запятая, чтобы Python понял, что это кортеж
                                                                       # из одного элемента.

    def test_schema_after_get_by_id(self, project_service: ProjectService, new_project_id):
        project_service.get_project_by_id(new_project_id)
        project_service.check_response_schema(expected_fields=('id', 'title'))