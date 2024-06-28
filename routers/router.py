from typing import List

from fastapi import APIRouter, Depends, File, UploadFile
from sqlalchemy.orm import Session

from db.database_definition import get_db

router = APIRouter(
    prefix="/",
    tags=[""],
)
