import enum
from typing import TYPE_CHECKING

from sqlalchemy import Enum, Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.config.database import Base
from app.models.report.reports import DepartmentType

if TYPE_CHECKING:
    from app.models.user.user_group import UserGroup


class DepartmentPosotionType(enum.Enum):
    admin = "Администратор"
    chief = "Начальник службы"
    master = "Мастер службы"


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(50), nullable=False, unique=True)
    password_hash: Mapped[str] = mapped_column(String, nullable=False)
    role: Mapped[str] = mapped_column(String(50), nullable=False)
    department_position: Mapped[DepartmentPosotionType] = mapped_column(Enum(DepartmentType, name="department type"), nullable=False)

    groups: Mapped[list[UserGroup]] = relationship(
        "UserGroup",
        back_populates="user"
    )
