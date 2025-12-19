from typing import TYPE_CHECKING

from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.config.database import Base

if TYPE_CHECKING:
    from app.models.report.report_rows import (
        ReportSection1Row,
        ReportSection2Row,
        ReportSection3Row,
    )


class Indicator(Base):
    __tablename__ = "indicators"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    code: Mapped[str] = mapped_column(String, nullable=False, unique=True)
    name: Mapped[str] = mapped_column(String, nullable=False, unique=True)


    report_section1_row: Mapped[ReportSection1Row] = relationship(
        "ReportSection1Row",
        back_populates="indicator"
    )

    report_section2_row: Mapped[ReportSection2Row] = relationship(
        "ReportSection2Row",
        back_populates="indicator"
    )

    report_section3_row: Mapped[ReportSection3Row] = relationship(
        "ReportSection3Row",
        back_populates="indicator"
    )
