from typing import TYPE_CHECKING

from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import Base

if TYPE_CHECKING:
    from .user import User


class ToDo(Base):
    __tablename__ = "todo"

    title: Mapped[str] = mapped_column(unique=True)
    description: Mapped[str] = mapped_column(String(length=500))
    status: Mapped[bool] = mapped_column(default=0)
    user_pk: Mapped[int] = mapped_column(ForeignKey("user.pk"))
    user: Mapped["User"] = relationship(back_populates='todos')

    def __repr__(self):
        return f"<ToDo(pk={self.pk}, title={self.title})>"

    def __str__(self):
        return self.__repr__()
