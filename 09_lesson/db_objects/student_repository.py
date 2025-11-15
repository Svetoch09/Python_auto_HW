from sqlalchemy import Table, select, insert, update, delete
from sqlalchemy.exc import NoSuchTableError
from db_objects.db_manager import DBManager


class StudentRepository:
    """Репозиторий для инкапсуляции всех операций с таблицей 'student'."""

    def __init__(self, db_manager: DBManager):
        self.db_manager = db_manager
        self.metadata = self.db_manager.get_metadata()
        self.student_table = self._load_table()

    def _ensure_table_exists(self):
        """Гарантирует существование таблицы 'student' перед ее отражением."""
        sql_create_table = """
            CREATE TABLE IF NOT EXISTS student (
                user_id INTEGER PRIMARY KEY,
                level TEXT,
                education_form TEXT,
                subject_id INTEGER
            )
        """
        self.db_manager.execute_ddl(sql_create_table)

    def _load_table(self):
        """Отражает таблицу из БД."""
        self._ensure_table_exists()
        try:
            student_table = Table('student', self.metadata,
                                  autoload_with=self.db_manager.engine)
            print("✅ Таблица 'student' успешно отражена.")
            return student_table
        except NoSuchTableError as e:
            print(f"❌ Критическая ошибка: Таблица 'student' отсутствует. {e}")
            return None

    def get_by_id(self, user_id: int):
        """SELECT * FROM student WHERE user_id = :user_id"""
        if self.student_table is None:
            return None

        stmt = select(self.student_table).where(
            self.student_table.c.user_id == user_id
        )
        with self.db_manager.connect() as conn:
            return conn.execute(stmt).fetchone()

    def create_student(self, user_id: int, level: str, form: str,
                       subject_id: int):
        """INSERT в таблицу student """
        if self.student_table is None:
            return 0   # ! тк возвращаем число созданных строк

        stmt = insert(self.student_table).values(
            user_id=user_id,
            level=level,
            education_form=form,
            subject_id=subject_id
        )
        with self.db_manager.connect() as conn:
            result = conn.execute(stmt)
            conn.commit()
            return result.rowcount

    def update_level(self, user_id: int, new_level: str):
        """UPDATE уровня студента """
        if self.student_table is None:
            return 0   # тк возвращаем число измен. строк

        stmt = update(self.student_table).where(
            self.student_table.c.user_id == user_id
        ).values(
            level=new_level
        )
        with self.db_manager.connect() as conn:
            result = conn.execute(stmt)
            conn.commit()
            return result.rowcount

    def delete_student(self, user_id: int):
        """DELETE студента по ID """
        if self.student_table is None:
            return 0

        stmt = delete(self.student_table).where(
            self.student_table.c.user_id == user_id
        )
        with self.db_manager.connect() as conn:
            result = conn.execute(stmt)
            conn.commit()
            return result.rowcount
