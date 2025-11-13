import pytest
from config import connection_string, test_user_id
from db_objects.db_manager import DBManager
from db_objects.student_repository import StudentRepository


@pytest.fixture(scope="session")
def db_manager():
    """Фикстура, создающая DBManager один раз за сеанс"""
    manager = DBManager(connection_string, echo=False)
    yield manager
    print("\n[conftest] db_manager фикстура завершена.")


@pytest.fixture(scope="session")
def student_repo(db_manager):
    """
    Фикстура, создающая StudentRepository и управляющая тестовыми данными.
    scope="session" обеспечивает единый объект репозитория для всех тестов.
    """
    repo = StudentRepository(db_manager)
    # Очистка тестовых данных перед запуском сеанса
    repo.delete_student(test_user_id)

    yield repo

    # TEARDOWN: Очистка тестовых данных после завершения сеанса
    repo.delete_student(test_user_id)
    print("\n[conftest] student_repo фикстура завершена."
          " Тестовые данные очищены.")
