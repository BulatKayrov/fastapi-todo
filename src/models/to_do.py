from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from .base import Base


class ToDo(Base):
    __tablename__ = "todo"

    title: Mapped[str] = mapped_column(unique=True)
    description: Mapped[str] = mapped_column(String(length=500))
    status: Mapped[bool] = mapped_column(default=0)

    def __repr__(self):
        return f"<ToDo(pk={self.pk}, title={self.title})>"

    def __str__(self):
        return self.__repr__()
