from typing import Any

from sqlalchemy import Integer, Column
from sqlalchemy.orm import declarative_base

Base: Any = declarative_base()


class SomeModel(Base):
    __tablename__ = "SomeModel"
    id = Column(Integer, primary_key=True)
    a = Column(Integer)
