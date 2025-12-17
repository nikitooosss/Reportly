from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.config.database import Base
from app.models.user.user_group import UserGroup


class Group(Base):
    __tablename__ = "groups"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(50), nullable=False, unique=True)


    users: Mapped[list[UserGroup]] = relationship(
        "UserGroup",
        back_populates="group"
    )
