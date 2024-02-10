import sqlite3
import datetime
from pathlib import Path
import os


class Clients():

    def __init__(self):
        self._statement = """
            CREATE TABLE IF NOT EXISTS input_log (
                id INTEGER PRIMARY KEY,
                Timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
                input_text TEXT,
                AI_Response TEXT
            )
        """

    def check_set_db(self):
        self.current_date = datetime.date.today().strftime("%Y-%m-%d")
        self.path = Path(f"DB/{self.current_date}")

        if self.path.is_dir():
            self.current_path = self.path / "requests.db"
            return self.current_path
        else:
            os.makedirs(self.path, exist_ok=True)
            self.db_path = self.path / "requests.db"

            self.conn = sqlite3.connect(self.db_path)
            self.cursor = self.conn.cursor()
            try:
                self.cursor.execute(self._statement)
                self.conn.commit()
                print("Table created successfully")
            except sqlite3.Error as e:
                print(f"Error creating table: {e}")

            self.cursor.close()
            self.conn.close()

            return self.db_path

    def insert_user(self, request):
        request = request[0]
        current_path = self.check_set_db()
        self.data_table = sqlite3.connect(current_path)
        self.cursor = self.data_table.cursor()

        self.cursor.execute("INSERT INTO input_log (input_text, AI_Response) VALUES (?, ?)", (
            request['input_text'], request["AI_Response"]))

        self.data_table.commit()

        self.cursor.close()
        self.data_table.close()
