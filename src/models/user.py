from typing import TYPE_CHECKING

from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import Base

if TYPE_CHECKING:
    from .to_do import ToDo


class User(Base):
    __tablename__ = "user"

    username: Mapped[str] = mapped_column(unique=True)
    hashed_password: Mapped[str]
    email: Mapped[str] = mapped_column(unique=True)

    todos: Mapped["ToDo"] = relationship(back_populates="user")

    def __repr__(self):
        return "<User(username=%r)>" % self.username

    def __str__(self):
        return self.__repr__()
