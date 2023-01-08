from fastapi import FastAPI, Request, Response, HTTPException, Depends, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from fastapi.middleware.cors import CORSMiddleware

import database, security
from models import DataDump, Vector, Admin, Token

# Build REST API
app = FastAPI()

# Set Cross Origin Policy
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.on_event("startup")
def startup_event():
    print("Startup")


@app.get("/", status_code=200)
async def root():
    return "Welcome to Flying Forward 2020"


@app.get("/api/users", status_code=200)
async def get_total_user_count():
    users = database.get_multiple_users()
    total = len(users)
    return {"total_users": total}


@app.post("/api/dump", status_code=200)
async def post_data(d: DataDump, request: Request, response: Response):
    # Validate Age
    if 0 > d.user_data.age > 100:
        raise HTTPException(status_code=400, detail="Age outside of normal bounds")

    if d.user_data.gender != 'm' and d.user_data.gender != 'f' and d.user_data.gender != 'o':
        raise HTTPException(status_code=400, detail="Gender must be male (m), female (f), or other (o)")

    user_id = database.add_new_user(d)
    for vector in d.vectors:
        success = database.add_vector(user_id, vector)
        if not success:
            raise HTTPException(status_code=400, detail=f"Failed to save {vector} to {user_id}")

    response.headers["Access-Control-Allow-Origin"] = "*"
    return {"msg": "user created",
            "user_id": user_id}


@app.get("/api/get_vectors/{user_id}", status_code=200)
async def get_vectors_by_user_id(user_id: int):
    user = database.get_one_user(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    vectors = database.get_multiple_vectors(user_id)
    if not vectors:
        raise HTTPException(status_code=404, detail="User not found")

    return vectors


@app.get("/api/user/{user_id}", status_code=200)
async def get_user_data_by_user_id(user_id: int):
    user = database.get_one_user(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return {user_id: user}


@app.post("/token", response_model=Token)
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    user = security.authenticate_user(form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token = security.create_access_token(data={"sub": user.username})
    return {"access_token": access_token, "token_type": "bearer"}


@app.get("/users/me/", response_model=Admin)
async def read_users_me(current_user: Admin = Depends(security.get_current_active_user)):
    return current_user


@app.get("/users/me/items/")
async def read_own_items(current_user: Admin = Depends(security.get_current_active_user)):
    return [{"item_id": "Foo", "owner": current_user.username}]
