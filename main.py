#taskkill /F /IM python.exe
from fastapi import FastAPI

import models
from database import engine

models.Base.metadata.create_all(bind=engine)

from post import post_router
from user import user_router
# from study import study_router

app = FastAPI()

app.include_router(post_router.app, tags = ["post"])
app.include_router(user_router.app, tags = ["user"])
#
# app.include_router(study_router.app, tags = ["study"])

@app.get("/")
def read_root():
    return {"Hello":"World"}