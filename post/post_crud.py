from h11 import Request
from sqlalchemy import func
from sqlalchemy.orm import Session
from post import post_schema
from models import Post, PostCategory, Category
from user import user_crud
from post import post_schema

def create_post(new_post: post_schema.CreatePost, db: Session):
    post = Post(content=new_post.content)

    # 카테고리가 None이 아니면
    if new_post.category:
        categories = db.query(Category)\
            .filter(Category.no.in_(new_post.category)).all()
        #Post와 Category 중간 테이블인 PostCategory 테이블에 데이터 삽입
        post.categories = categories

    db.add(post)
    db.commit()
    db.refresh(post)

    return {"message": "Post created"}

def create_new_category(new_category: str, db: Session):
    category = Category(category=new_category)
    db.add(category)
    db.commit()
    db.refresh(category)

    return {"message" : "Category created"}

def random_post(db: Session):
    post = db.query(Post).order_by(func.random()).first()
    return post

def custom_post(sort: post_schema.CreationOrder
                , db: Session
                , category_no: list[int] | None = None):
    #기본 쿼리 설정
    query = db.query(Post)
    #카테고리 선택시 필터링(0은 기본값)
    #입력받은 카테고리만 나오게 추출후 각 게시판별 카테고리 수가 크거나 같으면 추출
    if category_no and category_no[0] != 0:
        query = query.join(PostCategory)\
        .filter(PostCategory.category_no.in_(category_no))\
        .group_by(Post.no).having(
            func.count(PostCategory.category_no) >= (len(category_no))
        )

    if sort == "latest":
        post = query.order_by(Post.date.desc()).first()
    elif sort == "oldest":
        post = query.order_by(Post.date.asc()).first()
    else:
        post = query.order_by(func.random()).first()

    return post

def category_list(db: Session):
    categories= db.query(Category).all()
    return categories

# def pressed_like(db: Session):



