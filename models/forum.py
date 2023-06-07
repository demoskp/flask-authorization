from sqlalchemy import Column, Integer, String

from extensions import db


class Post(db.Model):
    __tablename__ = "posts"

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(80), nullable=False)
    body = Column(String(300), nullable=False)
