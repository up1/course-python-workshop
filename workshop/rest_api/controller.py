from fastapi import HTTPException, status
import mysql.connector
from database import Database
from models import DBModel

class UserController:
    def __init__(self):
        self.db = Database()

    def get_users(self):
        return self.db.get_all_users()

    def get_user_by_id(self, user_id: int):
        result = self.db.get_user_by_id(user_id)
        if result:
            return result
        else:
            raise HTTPException(status_code=404, detail="User not found")

    def create_user(self, user: DBModel):
        try:
            self.db.create_user(user)
            return {"message": "User inserted successfully"}
        except mysql.connector.Error as err:
            raise HTTPException(status_code=400, detail=f"Error: {err}")

    def update_user(self, user_id: int, user: DBModel):
        rows_affected = self.db.update_user(user_id, user)
        if rows_affected == 0:
            raise HTTPException(status_code=404, detail="User not found")
        return {"message": "User updated successfully"}

    def delete_user(self, user_id: int):
        rows_affected = self.db.delete_user(user_id)
        if rows_affected == 0:
            raise HTTPException(status_code=404, detail="User not found")
        return {"message": "User deleted successfully"}
