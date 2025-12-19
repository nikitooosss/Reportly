import enum
from datetime import date
from typing import TYPE_CHECKING

from sqlalchemy import Date, Enum, Integer
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.config.database import Base

if TYPE_CHECKING:
    from app.models.report.report_rows import (
        ReportSection1Row,
        ReportSection2Row,
        ReportSection3Row,
        ReportSection4Row,
    )


class ReportStatus(enum.Enum):
    not_started = "Не начат"
    in_work = "В работе"
    done = "Готов"


class ReportType(enum.Enum):
    weekly = "Недельный отчет"
    weekly_summary = "Недельная сводка"
    monthly_summary = "Месячная сводка"
    quarterly_summary = "Квартальная сводка"
    yearly_summary = "Годовая сводка"


class DepartmentType(enum.Enum):
    asu_a_tm = "АСУ, А и ТМ"


class Report(Base):
    __tablename__ = "reports"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    department_type: Mapped[DepartmentType] = mapped_column(Enum(DepartmentType, name="department type"), nullable=False)
    report_type: Mapped[ReportType] = mapped_column(Enum(ReportType, name="report type"), nullable=False)
    period_from: Mapped[date] = mapped_column(Date, nullable=False)
    period_to: Mapped[date] = mapped_column(Date, nullable=False)
    created_at: Mapped[date] = mapped_column(Date, nullable=False)
    created_by_id: Mapped[int] = mapped_column(Integer, nullable=False)
    status: Mapped[ReportStatus] = mapped_column(Enum(ReportStatus, name="report status"), nullable=False)

    report_section1_row: Mapped[list[ReportSection1Row]] = relationship(
            "ReportSection1Row",
            back_populates="report"
        )
    report_section2_row: Mapped[list[ReportSection2Row]] = relationship(
            "ReportSection2Row",
            back_populates="report"
        )
    report_section3_row: Mapped[list[ReportSection3Row]] = relationship(
            "ReportSection3Row",
            back_populates="report"
        )
    report_section4_row: Mapped[list[ReportSection4Row]] = relationship(
            "ReportSection4Row",
            back_populates="report"
        )
