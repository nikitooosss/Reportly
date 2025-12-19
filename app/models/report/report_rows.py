from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.config.database import Base

if TYPE_CHECKING:
    from app.models.report.indicators import Indicator
    from app.models.report.reports import Report
    from app.models.report.violation_categories import ViolationCategory


class ReportSection1Row(Base):
    __tablename__ = "report_section1_rows"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    report_id: Mapped[int] = mapped_column(
        ForeignKey("reports.id"),
        nullable=False
    )
    indicator_id: Mapped[int] = mapped_column(
        ForeignKey("indicators.id"),
        nullable=False
    )
    violation_category_id: Mapped[int | None] = mapped_column(
        ForeignKey("violation_categories.id"),
        nullable=True
    )
    total_count: Mapped[int | None] = mapped_column(Integer, nullable=True, default=0)
    influence_dangerous_event: Mapped[int | None] = mapped_column(Integer, nullable=True, default=0)
    level_1_count: Mapped[int | None] = mapped_column(Integer, nullable=True, default=0)
    level_1_influence: Mapped[int | None] = mapped_column(Integer, nullable=True, default=0)
    level_2_count: Mapped[int | None] = mapped_column(Integer, nullable=True, default=0)
    level_2_influence: Mapped[int | None] = mapped_column(Integer, nullable=True, default=0)
    state_violations_count: Mapped[int | None] = mapped_column(Integer, nullable=True, default=0)

    # For №1.7
    text_value: Mapped[str | None] = mapped_column(String, nullable=True, default='')

    report: Mapped[Report] = relationship(
        "Report",
        back_populates="report_section1_row"
    )
    violation_category: Mapped[ViolationCategory] = relationship(
        "ViolationCategory",
        back_populates="report_section1_row"
    )
    indicator: Mapped[Indicator] = relationship(
        "Indicator",
        back_populates="report_section1_row"
    )


class ReportSection2Row(Base):
    __tablename__ = "report_section2_rows"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    report_id: Mapped[int] = mapped_column(
        ForeignKey("reports.id"),
        nullable=False
    )
    indicator_id: Mapped[int] = mapped_column(
        ForeignKey("indicators.id"),
        nullable=False
    )
    total_count: Mapped[int | None] = mapped_column(Integer, nullable=True, default=0)
    total_level_1_count: Mapped[int | None] = mapped_column(Integer, nullable=True, default=0)
    total_level_2_count: Mapped[int | None] = mapped_column(Integer, nullable=True, default=0)
    total_state_violations_count: Mapped[int | None] = mapped_column(Integer, nullable=True, default=0)

    report: Mapped[Report] = relationship(
        "Report",
        back_populates="report_section2_row"
    )
    indicator: Mapped[Indicator] = relationship(
        "Indicator",
        back_populates="report_section2_row"
    )


class ReportSection3Row(Base):
    __tablename__ = "report_section3_rows"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    report_id: Mapped[int] = mapped_column(
        ForeignKey("reports.id"),
        nullable=False
    )
    indicator_id: Mapped[int] = mapped_column(
        ForeignKey("indicators.id"),
        nullable=False
    )

    total_level_1_talks_count: Mapped[int] = mapped_column(Integer, nullable=True, default=0)
    total_level_2_talks_count: Mapped[int] = mapped_column(Integer, nullable=True, default=0)
    meetings: Mapped[int] = mapped_column(Integer, nullable=True, default=0)
    briefings: Mapped[int] = mapped_column(Integer, nullable=True, default=0)
    initial_briefings: Mapped[int] = mapped_column(Integer, nullable=True, default=0)
    re_briefings: Mapped[int] = mapped_column(Integer, nullable=True, default=0)
    targeted_briefings: Mapped[int] = mapped_column(Integer, nullable=True, default=0)
    unscheduled_briefings: Mapped[int] = mapped_column(Integer, nullable=True, default=0)

    report: Mapped[Report] = relationship(
        "Report",
        back_populates="report_section3_row"
    )
    indicator: Mapped[Indicator] = relationship(
        "Indicator",
        back_populates="report_section3_row"
    )


class ReportSection4Row(Base):
    __tablename__ = "report_section4_rows"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)

    message: Mapped[str | None] = mapped_column(String, nullable=True)

    report_id: Mapped[int] = mapped_column(
        ForeignKey("reports.id"),
        nullable=False
    )

    report: Mapped[Report] = relationship(
        "Report",
        back_populates="report_section4_row"
    )
