from datetime import timedelta, datetime, timezone
import os
from jose import jwt
from passlib.context import CryptContext
from sqlalchemy.orm import Session
from dotenv import load_dotenv
import models
from user import user_schema, user_router
from fastapi import HTTPException, status, Response,Request
from starlette.responses import JSONResponse

pwd_context = CryptContext(schemes = ["bcrypt"], deprecated="auto")
load_dotenv()
SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = os.getenv("ALGORITHM")
ACCESS_TOKEN_EXPIRE_MINUTES = float(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES"))

def get_user(id: str, db: Session):
    return db.query(models.User).filter(models.User.user_id == id).first()

def get_email(email: str, db: Session):
    return db.query(models.User).filter(models.User.email == email).first()

def create_user(new_user: user_schema.CreateUserForm, db: Session):
    db_user = get_user(new_user.id, db)
    db_email = get_email(new_user.email, db)

    #아이디 중복 체크
    if db_user:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="id is already exists")
    #이메일 중복 체크
    if db_email:
        raise HTTPException(status_code = status.HTTP_409_CONFLICT, detail="email is already exists")
    #비번, 비번확인 둘이 맞는지 체크
    if not new_user.password == new_user.password_confirm:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="Password does not match")
    # 회원가입
    user = models.User(
        name = new_user.username,
        user_id = new_user.id,
        email = new_user.email,
        hashed_password = pwd_context.hash(new_user.password),

    )
    db.add(user)
    db.commit()
    db.refresh(user)

    return {"message" : "Signup successful"}

def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

def create_access_token(data: dict, expires_delta: timedelta | None = None):
    to_encode = data.copy()
    #주어진 ACCESS_TOKEN_EXPIRE_MINUTES = 15 값이 잘 넘어 왔을때
    if expires_delta:
        #현재 시간 + ACCESS_TOKEN_EXPIRE_MINUTES = 15 값
        expire = datetime.utcnow() + expires_delta
    else:
        #현재 시간 + 임의의 값 15분
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

def decode_access_token(token: str):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=ALGORITHM)
        return payload
    except jwt.JWTError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token")

def login(response : Response, login_form : user_schema.LoginForm, db: Session):
    # 아이디 존재 확인
    db_user = get_user(login_form.id, db)

    if not db_user:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Invalidd username or password")

    # 비밀번호 체크
    res = verify_password(login_form.password, db_user.hashed_password)
    #비밀번호 없을 경우
    if not res:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid username or password")

    #토큰 만료 시간 설정
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    #토큰 생성
    access_token = create_access_token(data = {"email": db_user.email}, expires_delta = access_token_expires)
    #쿠키 만료 시간 ( 세계 시간 utc로 설정 )
    cookie_expiration = (datetime.utcnow() + access_token_expires).replace(tzinfo=timezone.utc)
    #쿠키에 저장
    response.set_cookie(key = "access_token", value = access_token, expires=cookie_expiration ,httponly=True)

    return {"message": "Login successful"}

def logout(response: Response, request: Request):
    #쿠키의 키 값의 이름을 바탕으로 가져옴
    access_token = request.cookies.get("access_token")
    #로그인이 안 되어 있거나 이미 토큰이 없음
    if not access_token:
        raise HTTPException(status_code=400, detail="Token is not found")
    # 쿠키 삭제
    response.delete_cookie(key="access_token")

    return {"message": "Logout successful"}

def get_current_user(request: Request) -> dict:
    token = request.cookies.get("access_token")
    #유저 인증이 안 됨
    if not token:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Not authenticated")

    user_data = decode_access_token(token)
    return user_data

def is_admin(request: Request) -> bool:
    account = get_current_user(request)
    if account["position"] == "MANAGER":
        return True
    else:
        return False
