import uvicorn
from fastapi import FastAPI, Request
from pydantic import BaseModel
from typing import List

app = FastAPI()


class Position(BaseModel):
    time: int
    x: float
    y: float
    z: float

    def __str__(self):
        return f"{self.time},{self.x},{self.y},{self.z}"


class DataDump(BaseModel):
    map: str
    positions: List[Position] = []

    def __str__(self):
        s = (self.map + "\n")
        for pos in self.positions:
            s += str(pos)
            s += "\n"
        return s


@app.post("/data", status_code=200)
def post_data(data: DataDump, request: Request):
    print(data)


@app.post("/pos", status_code=200)
def post_data(pos: Position, request: Request):
    print(pos)


if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=8080)
