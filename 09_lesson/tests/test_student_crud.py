import pytest
from config import test_user_id


@pytest.mark.positive
class TestStudentCRUD:
    """Тесты, проверяющие операции CRUD с таблицей student."""

    def test_01_insert_and_select(self, student_repo):
        student_repo.delete_student(test_user_id)

        # ДОБАВЛЕНИЕ студента (1 запись в таблицу)
        rows_added = student_repo.create_student(
            test_user_id, 'Native', 'personal', 1)
        assert rows_added == 1, "❌ INSERT: Добавлена 0 строк."

        # SELECT и Проверка
        student_data = student_repo.get_by_id(test_user_id)

        assert student_data is not None, \
            f"❌ SELECT: Студент с ID {test_user_id} не найден."
        assert student_data.level == 'Native', \
            "❌ SELECT: Уровень не совпадает с ожидаемым."

    def test_02_update_student_level(self, student_repo):
        """Проверяет обновление данных студента."""

        student_repo.delete_student(test_user_id)
        student_repo.create_student(test_user_id, 'Native', 'personal', 1)

        NEW_LEVEL = 'Expert'

        rows_updated = student_repo.update_level(test_user_id, NEW_LEVEL)

        assert rows_updated == 1, "❌ UPDATE: Изменена 0 строк."

        # SELECT и Проверка
        updated_data = student_repo.get_by_id(test_user_id)
        assert updated_data.level == NEW_LEVEL, \
            "❌ UPDATE: Уровень не был изменен на 'Expert'."

    def test_03_delete_student(self, student_repo):
        """Проверяет удаление записи."""

        student_repo.delete_student(test_user_id)
        student_repo.create_student(test_user_id, 'Native', 'personal', 1)

        rows_deleted = student_repo.delete_student(test_user_id)
        assert rows_deleted == 1, "❌ DELETE: Удалена 0 строк."

        # проверка что записи в БД нет
        deleted_data = student_repo.get_by_id(test_user_id)
        assert deleted_data is None, \
            f"❌ DELETE: Студент с ID {test_user_id} не был удален."
