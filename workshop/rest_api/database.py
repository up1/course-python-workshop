import mysql.connector
import hashlib
from typing import List, Tuple, Optional
from models import DBModel

class Database:
    def __init__(self):
        self.mydb = mysql.connector.connect(
            host="localhost",
            user="user01",
            password="password01",
            database="my_database"
        )
        self.cursor = self.mydb.cursor()

    def get_all_users(self) -> List[Tuple]:
        select_query = "SELECT * FROM users"
        self.cursor.execute(select_query)
        return self.cursor.fetchall()

    def get_user_by_id(self, user_id: int) -> Optional[Tuple]:
        select_query = "SELECT * FROM users WHERE id = %s"
        self.cursor.execute(select_query, (user_id,))
        return self.cursor.fetchone()

    def create_user(self, user: DBModel) -> None:
        hashed_password = hashlib.sha256(user.password.encode()).hexdigest()
        insert_query = """
        INSERT INTO users (username, password, email)
        VALUES (%s, %s, %s)
        """
        values = (user.username, hashed_password, user.email)
        self.cursor.execute(insert_query, values)
        self.mydb.commit()

    def update_user(self, user_id: int, user: DBModel) -> int:
        hashed_password = hashlib.sha256(user.password.encode()).hexdigest()
        update_query = """
        UPDATE users
        SET username = %s, password = %s, email = %s
        WHERE id = %s
        """
        values = (user.username, hashed_password, user.email, user_id)
        self.cursor.execute(update_query, values)
        self.mydb.commit()
        return self.cursor.rowcount

    def delete_user(self, user_id: int) -> int:
        delete_query = "DELETE FROM users WHERE id = %s"
        self.cursor.execute(delete_query, (user_id,))
        self.mydb.commit()
        return self.cursor.rowcount

    def close(self):
        self.cursor.close()
        self.mydb.close()
