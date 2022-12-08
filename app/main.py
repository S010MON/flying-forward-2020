import uvicorn
from fastapi import FastAPI, Request
from pydantic import BaseModel
from typing import List
from mysql.connector import (connection)
import mysql.connector

# Docker config
config = {'user': 'root',
          'password': 'password',
          'host': 'db',
          'port': '3306',
          'database': 'drone'
          }

# Setup SQL connector
cnx = mysql.connector.connect(**config)
cursor = cnx.cursor()

# Build REST API
app = FastAPI()


class UserRequest(BaseModel):
    age: int
    flying_minutes: int
    gender: str
    licences: str


class Position(BaseModel):
    time: int
    x: float
    y: float
    z: float

    def __str__(self):
        return f"{self.time},{self.x},{self.y},{self.z}"


class DataDump(BaseModel):
    user_id: int
    map: str
    positions: List[Position] = []

    def __str__(self):
        s = (self.map + "\n")
        for pos in self.positions:
            s += str(pos)
            s += "\n"
        return s


@app.get("/", status_code=200)
def root():
    return "Welcome to Flying Forward 2020!"


@app.post("/user", status_code=200)
def new_user(user: UserRequest, request: Request):
    # Insert new user
    query = f"INSERT INTO Users (age, flying_minutes, gender, licences) VALUES (" \
            f"{user.age}," \
            f"{user.flying_minutes}," \
            f"\"{user.gender}\"," \
            f"\"{user.licences}\");"
    cursor.execute(query)

    # Fetch new user_id
    query = "SELECT LAST_INSERT_ID()";
    cursor.execute(query)
    result = cursor.fetchone()
    return {"user_id": result}


@app.post("/data", status_code=200)
def post_data(data: DataDump, request: Request):
    # generate a new session
    query = f"INSERT INTO Sessions (user_id, map) VALUES ({data.user_id}, \"{data.map}\");"
    cursor.execute(query)

    # Fetch new session_id
    query = "SELECT LAST_INSERT_ID()";
    cursor.execute(query)
    result = cursor.fetchone()
    print(f"Created new session: {result}")


if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=8080)
