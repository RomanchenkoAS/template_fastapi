from fastapi import FastAPI
from db import models
from db.database_definition import engine

app = FastAPI()


models.Base.metadata.create_all(bind=engine)
