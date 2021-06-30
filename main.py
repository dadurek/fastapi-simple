from fastapi import FastAPI
from Utils import  models
from Utils.database import engine
from Routers import item, user

app = FastAPI()

models.Base.metadata.create_all(engine)

app.include_router(user.router)
app.include_router(item.router)