from fastapi import FastAPI, status
from controller import UserController
from models import DBModel

app = FastAPI()
user_controller = UserController()

@app.get("/users", status_code=status.HTTP_200_OK)
def select_users():
    return user_controller.get_users()

@app.get("/users/{user_id}", status_code=status.HTTP_200_OK)
def get_user_by_id(user_id: int):
    return user_controller.get_user_by_id(user_id)

@app.post("/users", status_code=status.HTTP_201_CREATED)
def insert_user(user: DBModel):
    return user_controller.create_user(user)

@app.put("/users/{user_id}", status_code=status.HTTP_200_OK)
def update_user(user_id: int, user: DBModel):
    return user_controller.update_user(user_id, user)

@app.delete("/users/{user_id}", status_code=status.HTTP_200_OK)
def delete_user(user_id: int):
    return user_controller.delete_user(user_id)