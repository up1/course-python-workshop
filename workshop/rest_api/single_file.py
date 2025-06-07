# !pip install fastapi uvicorn pydantic mysql-connector-python

from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel
import mysql.connector
import hashlib

# Data model
class DBModel(BaseModel):
    username: str
    password: str
    email: str

# Database connection
mydb = mysql.connector.connect(
    host="localhost",
    user="user01",
    password="password01",
    database="my_database"
)

# Create a cursor object
cursor = mydb.cursor()

app = FastAPI()

# Get all users
@app.get("/users", status_code=status.HTTP_200_OK)
def select_users():
    select_query = "SELECT * FROM users"
    cursor.execute(select_query)
    results = cursor.fetchall()
    return results

# Create a new user
@app.post("/users", status_code=status.HTTP_201_CREATED)
def insert_user(user: DBModel):
    # Hash the password using SHA-256
    hashed_password = hashlib.sha256(user.password.encode()).hexdigest()

    insert_query = """
    INSERT INTO users (username, password, email)
    VALUES (%s, %s, %s)
    """
    values = (user.username, hashed_password, user.email)

    try:
        cursor.execute(insert_query, values)
        mydb.commit()
    except mysql.connector.Error as err:
        raise HTTPException(status_code=400, detail=f"Error: {err}")

    return {"message": "User inserted successfully"}