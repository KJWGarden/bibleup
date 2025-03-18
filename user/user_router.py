from database import get_db
from fastapi import APIRouter, Response, Request
from sqlalchemy.orm import Session
from fastapi.params import Depends
from user import user_schema, user_crud

app = APIRouter(
    prefix="/users",
)


@app.post(path="/signup")
async def signup(new_user: user_schema.CreateUserForm = Depends(), db:Session = Depends(get_db)):
    return user_crud.create_user(new_user, db)

@app.post("/login")
async def login(response: Response, login_form: user_schema.LoginForm = Depends(), db: Session = Depends(get_db)):
    return user_crud.login(response, login_form, db)

@app.get(path="/logout")
async def logout(response: Response, request: Request):
    return user_crud.logout(response, request)
