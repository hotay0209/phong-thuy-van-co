from datetime import datetime, timezone
from sqlalchemy import DateTime, Float, Integer, String, Text
from sqlalchemy.orm import Mapped, mapped_column
from .database import Base

class HouseAnalysis(Base):
    __tablename__ = "house_analyses"
    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    house_name: Mapped[str] = mapped_column(String(160), default="Nhà ở")
    address: Mapped[str | None] = mapped_column(String(300), nullable=True)
    construction_year: Mapped[int] = mapped_column(Integer)
    facing_degrees: Mapped[float] = mapped_column(Float)
    facing_mountain: Mapped[str] = mapped_column(String(8))
    sitting_mountain: Mapped[str] = mapped_column(String(8))
    period_number: Mapped[int] = mapped_column(Integer)
    result_json: Mapped[str] = mapped_column(Text)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc))
