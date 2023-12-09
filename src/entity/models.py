from datetime import date
from sqlalchemy.orm import Mapped, mapped_column, DeclarativeBase
from sqlalchemy import String, Date, Text, DateTime, func, Integer


class Base(DeclarativeBase):
    pass


class Contact(Base):
    __tablename__ = 'contacts'
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    firstname: Mapped[str] = mapped_column(String(50), index=True)
    lastname: Mapped[str] = mapped_column(String(50), index=True)
    email: Mapped[str] = mapped_column(String(30), index=True)
    phone: Mapped[str] = mapped_column(String(30), index=True)
    birthday: Mapped[date] = mapped_column(Date, index=True, nullable=True)
    additional_data: Mapped[str] = mapped_column(Text, nullable=True)
    created_at: Mapped[date] = mapped_column(DateTime, default=func.now())
    updated_at: Mapped[date] = mapped_column(DateTime, default=func.now(), onupdate=func.now())
