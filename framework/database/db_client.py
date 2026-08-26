import sqlite3


class DatabaseClient:

    def __init__(self, database_path):
        self.database_path = database_path

    def execute_query(self, query, parameters=()):
        connection = sqlite3.connect(self.database_path)

        try:
            cursor = connection.cursor()
            cursor.execute(query, parameters)
            return cursor.fetchall()
        finally:
            connection.close()

    def execute_update(self, query, parameters=()):
        connection = sqlite3.connect(self.database_path)

        try:
            cursor = connection.cursor()
            cursor.execute(query, parameters)
            connection.commit()
        finally:
            connection.close()