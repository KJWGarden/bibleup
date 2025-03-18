from fastapi import APIRouter, Depends, Request, Query
from sqlalchemy.orm import Session
from database import get_db
from post import post_crud, post_schema
from typing import Annotated

app = APIRouter(
    prefix = "/post",
)

@app.post("/create", description="게시판 생성 - 관리자 용")
async def create_new_post(create_post: post_schema.CreatePost ,db: Session = Depends(get_db)):
    return post_crud.create_post(create_post, db)

@app.post("/create/category", description="카테고리 생성 - 관리자 용")
async def create_category(new_category: str, db: Session = Depends(get_db)):
    return post_crud.create_new_category(new_category, db)

@app.get("/random", description="게시글 불러오기")
async def get_random_post(db: Session = Depends(get_db)):
    return post_crud.random_post(db)

@app.post("/custom", description="커스텀 랜덤 게시글 불러오기")
async def get_custom_post(sort: post_schema.CreationOrder
    , db: Session = Depends(get_db)
    , category_no: list[int] | None = None):
    return post_crud.custom_post(sort, db, category_no)

@app.get("/category/list", description="카테고리 목록")
async def get_category_list(db: Session = Depends(get_db)):
    return post_crud.category_list(db)

# @app.post("pressed/like", description="좋아요 버튼 눌렀을때")
# async def get_pressed_like(db, Session = Depends(get_db)):
#     return post_crud.pressed_like(db)


