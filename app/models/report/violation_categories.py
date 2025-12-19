from typing import TYPE_CHECKING

from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.config.database import Base

if TYPE_CHECKING:
    from app.models.report.reports import Report


class ViolationCategory(Base):
    __tablename__ = "violation_categories"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    code: Mapped[str] = mapped_column(String, nullable=False, unique=True)
    name: Mapped[str] = mapped_column(String, nullable=False, unique=True)

    report_section1_row: Mapped[Report] = relationship(
        "Report",
        back_populates="violation_category"
    )
