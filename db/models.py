from datetime import datetime, timezone

from sqlalchemy import (
    Boolean,
    Column,
    DateTime,
    ForeignKey,
    Integer,
    LargeBinary,
    String,
)
from sqlalchemy.orm import relationship

from db.database_definition import Base


def timestamp() -> datetime:
    return datetime.now(timezone.utc)


class DbBlogPost(Base):
    __tablename__ = "blog_posts_t"
    id = Column(Integer, primary_key=True)
    title = Column(String, unique=True, nullable=False)
    content = Column(String, nullable=True)
    image = Column(LargeBinary, nullable=True)
    date_posted = Column(DateTime, default=timestamp)
    date_updated = Column(DateTime, default=timestamp, onupdate=timestamp)

    # Foreign
    author_id = Column(Integer, ForeignKey("authors_t.id"), nullable=False)
    author = relationship("DbAuthor", back_populates="posts")

    def __repr__(self):
        return f"<BlogPost {self.id} '{self.title}'>"


class DbAuthor(Base):
    __tablename__ = "authors_t"
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True, nullable=False)
    last_posted = Column(DateTime, default=timestamp, nullable=True)
    is_admin = Column(Boolean, nullable=False, default=False)

    # Foreign
    posts = relationship("DbBlogPost", back_populates="author")

    def __repr__(self):
        return f"<Author {self.id} {self.name}>"
