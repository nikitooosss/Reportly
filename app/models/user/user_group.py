from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.config.database import Base
from app.models.user.groups import Group
from app.models.user.users import User


class UserGroup(Base):
    __tablename__ = "user_groups"

    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"), primary_key=True)
    group_id: Mapped[int] = mapped_column(ForeignKey("groups.id"), primary_key=True)

    user: Mapped[User] = relationship(
        "User",
        back_populates="groups"
    )
    group: Mapped[Group] = relationship(
        "Group",
        back_populates="users"
    )
