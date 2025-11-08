import pytest
from ProjectService import ProjectService

# --- КОНСТАНТЫ ---
NON_EXISTENT_ID = "00000000-0000-0000-0000-000000000000"
UPDATED_TITLE = "Измененное Название"

# ==============================================================================
#                            POST НЕГАТИВНЫЕ ТЕСТЫ
# ==============================================================================

class TestNegativeCreation:
    @pytest.mark.negative
    def test_negative_create_without_title(self, project_service: ProjectService):
        project_data = {"title": ""}
        project_service.create_project(project_data)
        project_service.check_response_status(expected_status=400)

    def test_negative_create_without_body(self, project_service: ProjectService):
        project_data = {}
        project_service.create_project(project_data)
        project_service.check_response_status(expected_status=400)


# ==============================================================================
#                            GET/PUT НЕГАТИВНЫЕ ТЕСТЫ
# ==============================================================================

class TestNegativeAccess:
    @pytest.mark.negative
    def test_negative_get_project_by_non_existent_id(self, project_service: ProjectService):
        non_existing_project_id = NON_EXISTENT_ID
        project_service.get_project_by_id(non_existing_project_id)
        project_service.check_response_status(expected_status=404)

    def test_negative_update_non_existent_id(self, project_service: ProjectService):
        non_existing_project_id = NON_EXISTENT_ID
        update_data = {"title": UPDATED_TITLE}
        project_service.update_project(non_existing_project_id, update_data)
        project_service.check_response_status(expected_status=404)

        # Очищаем ID фикстуры - не пытаться удалить его в TEARDOWN
        new_project_id = None
