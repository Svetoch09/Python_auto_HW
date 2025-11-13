from sqlalchemy import create_engine, MetaData, text
from contextlib import contextmanager


class DBManager:
    """Класс для управления подключением и базовыми объектами SQLAlchemy."""

    def __init__(self, connection_string, echo=False):
        self.engine = create_engine(connection_string, echo=echo)
        self.metadata = MetaData()

    @contextmanager
    def connect(self):
        # открытие и автоматическое закрытия соединения.
        conn = None
        try:
            conn = self.engine.connect()
            yield conn
        finally:
            if conn:
                conn.close()

    def get_metadata(self):
        # Возвращает объект MetaData
        return self.metadata

    def execute_ddl(self, sql_command):
        """Выполняет DDL-команду (CREATE, ALTER, DROP, TRUNCATE, RENAME)
                                              и фиксирует изменения."""
        with self.engine.connect() as conn:
            conn.execute(text(sql_command))
            conn.commit()
            print("✅ DDL-операция выполнена и зафиксирована.")
