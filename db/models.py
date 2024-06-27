from datetime import datetime, timezone

from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey
from sqlalchemy.orm import relationship

from db.database_definition import Base


def timestamp() -> datetime:
    return datetime.now(timezone.utc)


