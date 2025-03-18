from sqlalchemy import Column, Integer, VARCHAR, DateTime, ForeignKey
from datetime import datetime

from sqlalchemy.orm import relationship

from database import Base


class User(Base):
    __tablename__ = "User"

    no = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(VARCHAR(40), nullable=False, unique=True)
    email = Column(VARCHAR(100), nullable=False, unique=True)
    hashed_password = Column(VARCHAR(100), nullable=False)
    name = Column(VARCHAR(10), nullable=False, unique=True)
    position = Column(VARCHAR(20), nullable=False, default='MEMBER')  #기본적으로 멤버로 설정하고 테이블에 데이터 추가하여 관리자 설정
    regdate = Column(DateTime, nullable=False, default=datetime.now)

    #유저가 저장한 컬렉션
    collected_posts = relationship("Post", secondary="Collection", back_populates="users_collected")
    #유저가 좋아요한 게시글
    liked_posts = relationship("Post", secondary="Like", back_populates="users_liked")

class Post(Base):
    __tablename__="Post"

    no = Column(Integer, primary_key=True, autoincrement=True)
    content = Column(VARCHAR(100), nullable=False)
    date = Column(DateTime, default=datetime.now)

    #이 게시글에 속한 카테고리들
    categories = relationship("Category", secondary="PostCategory", back_populates="posts")
    #이 게시글을 컬렉션한 유저들
    users_collected = relationship("User", secondary="Collection", back_populates="collected_posts")
    #이 게시글을 좋아요한 유저들
    users_liked = relationship("User", secondary="Like", back_populates="liked_posts")

class Category(Base):
    __tablename__ = "Category"

    no = Column(Integer, primary_key=True, autoincrement=True)
    category = Column(VARCHAR(50), nullable=False, unique=True)

    #카테고리에 속한 게시글들
    posts = relationship("Post", secondary="PostCategory", back_populates="categories")

class PostCategory(Base):
    __tablename__ = "PostCategory"

    post_no = Column(Integer, ForeignKey("Post.no"), primary_key=True)
    category_no = Column(Integer, ForeignKey("Category.no"), primary_key=True)

class Collection(Base):
    __tablename__ = "Collection"

    user_no = Column(Integer, ForeignKey("User.no"), primary_key=True)
    post_no = Column(Integer, ForeignKey("Post.no"), primary_key=True)

class Like(Base):
    __tablename__ = "Like"

    user_no = Column(Integer, ForeignKey("User.no"), primary_key=True)
    post_no = Column(Integer, ForeignKey("Post.no"), primary_key=True)
