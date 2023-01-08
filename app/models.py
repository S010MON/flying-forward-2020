from pydantic import BaseModel
from typing import List


class Admin(BaseModel):
    username: str
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: str | None = None


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
