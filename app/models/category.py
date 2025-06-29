from sqlalchemy import String, Integer
from sqlalchemy.orm import relationship, Mapped, mapped_column
from . import Base
from typing import Optional

class Category(Base):
    """
    Represents a budget or transaction category in the Family Finance Manager system.

    :param id: Unique identifier for the category.
    :param name: Unique name of the category (e.g., Groceries, Utilities).
    :param description: Optional description of the category.
    """
    __tablename__ = "category"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(64), unique=True, nullable=False)
    description: Mapped[Optional[str]] = mapped_column(String(255), nullable=True)

    budgets = relationship("Budget", back_populates="category", cascade="all, delete-orphan")
    transactions = relationship("Transaction", back_populates="category", cascade="all, delete-orphan")

    def __init__(self, name: str, description: Optional[str]) -> None:
        super().__init__()
        self.name = name
        self.description = description

    def __repr__(self) -> str:
        return f"<Category(id={self.id}, name='{self.name}', description='{self.description}')>"
