import uvicorn
from fastapi import FastAPI, Request, HTTPException
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


class UserData(BaseModel):
    age: int
    flying_exp_mins: int
    gender: str
    license: str


class Summary(BaseModel):
    time_overflying_people_ms: int
    number_overflown_people: int
    min_dist_to_nearest_structure: float
    min_dist_to_nearest_person: float
    avg_dist_to_intruder: float
    max_dist_to_start: float
    gated_vul_points: int


class Vector(BaseModel):
    time_ms: int
    px: float
    py: float
    pz: float
    vx: float
    vy: float
    vz: float


class DataDump(BaseModel):
    user_data: UserData
    map: str
    summary: Summary
    vectors: List[Vector] = []

    def __str__(self):
        s = (self.map + "\n")
        for v in self.vectors:
            s += str(v)
            s += "\n"
        return s


@app.get("/", status_code=200)
def root():
    return "Welcome to Flying Forward 2020?"


counters = {}


@app.on_event("startup")
async def startup_event():
    counters['test'] = 0
    counters['user'] = 2


@app.get("/", status_code=200)
async def home():
    return "Welcome to Flying Forward 2020!"


@app.get("/api/count", status_code=200)
async def get_count():
    counters['test'] += 1
    return {"test_count": counters['test']}


@app.post("/api/dump", status_code=200)
async def post_data(d: DataDump, request: Request):
    # Validate Age
    if 0 > d.user_data.age > 100:
        print(f"User input incorrect: age {d.user_data.age}")
        raise HTTPException(status_code=400, detail="Age outside of normal bounds")

    if d.user_data.gender != 'm' and d.user_data.gender != 'f' and d.user_data.gender != 'o':
        print(f"User input incorrect: gender {d.user_data.data}")
        raise HTTPException(status_code=400, detail="Gender must be male (m), female (f), or other (o)")

    user_id = add_new_user(d)
    print(f"INFO: user created: {user_id}")
    for v in d.vectors:
        add_vector(user_id, v)

    return {"msg": "user created",
            "user_id": user_id}


def add_new_user(d: DataDump):
    """
    Add a new user and return the integer user_id from the new user
    """
    # Fetch new user_id
    counters['user'] += 1
    query = f"INSERT INTO Users (age, flying_minutes, gender, licences,  time_overflying_people_ms, number_overflown_people, " \
            f"min_dist_to_nearest_structure, min_dist_to_nearest_person, avg_dist_to_intruder, max_dist_to_start, " \
            f"gated_vul_points, map) VALUES " \
            f"({d.user_data.age}, " \
            f"{d.user_data.flying_exp_mins}, " \
            f"\"{d.user_data.gender}\", " \
            f"\"{d.user_data.license}\", " \
            f"{d.summary.time_overflying_people_ms}, " \
            f"{d.summary.number_overflown_people}, " \
            f"{d.summary.min_dist_to_nearest_structure}, " \
            f"{d.summary.min_dist_to_nearest_person}, " \
            f"{d.summary.avg_dist_to_intruder}, " \
            f"{d.summary.max_dist_to_start}, " \
            f"{d.summary.gated_vul_points}, " \
            f"\"{d.map}\");"
    cursor.execute(query)
    return counters['user']


@app.get("/get_vectors/{user_id}", status_code=200)
async def get_data_by_user_id(user_id: int):
    query = f"SELECT * FROM Users where user_id = {user_id}"
    cursor.execute(query)
    if not cursor.fetchone():
        return HTTPException(status_code=404, detail="user not found")


    query = f"SELECT time_ms, px, py, px, vx, vy, vz FROM Vectors WHERE user_id = {user_id}"
    cursor.execute(query)
    result = cursor.fetchall()

    i = 0
    response = {}
    for line in result:
        p = {'x': line[1], 'y': line[2], 'z': line[3]}
        v = {'x': line[4], 'y': line[5], 'z': line[6]}
        response[i] = {'time_ms': line[0], 'p': p, 'v': v}
        i += 1

    return response


@app.get("/pull/{password}", status_code=200)
async def pull_data(password: str):
    query = "SELECT * FROM Users"
    cursor.execute(query)
    result = cursor.fetchall()
    D = {}
    i = 0
    for line in result:
        D[i] = result

    return D


def add_vector(user_id: int, vector: Vector):
    query = f"INSERT INTO Vectors (user_id, time_ms, px, py, pz, vx, vy, vz) VALUES (" \
            f"{user_id}," \
            f"{vector.time_ms}," \
            f"{vector.px}," \
            f"{vector.py}," \
            f"{vector.pz}," \
            f"{vector.vx}," \
            f"{vector.vy}," \
            f"{vector.vz});"
    cursor.execute(query)


if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=8080)
