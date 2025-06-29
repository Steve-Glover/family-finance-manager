from typing import Optional
from sqlalchemy import String, Integer, ForeignKey
from sqlalchemy.orm import relationship, Mapped, mapped_column
from . import Base
from typing import Optional


class Budget(Base):
    """
    Represents a planned spending budget for a user, category, and period.

    :param id: Unique identifier for the budget.
    :param user_id: Foreign key referencing the user.
    :param category_id: Foreign key referencing the category.
    :param amount: The budgeted amount.
    :param period: The budget period (e.g., "2025-07").
    :param description: Optional description of the budget.
    """

    __tablename__ = "budget"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    user_id: Mapped[int] = mapped_column(Integer, ForeignKey("user.id"), nullable=False)
    category_id: Mapped[int] = mapped_column(Integer, ForeignKey("category.id"), nullable=False)
    amount: Mapped[float] = mapped_column(nullable=False)
    period: Mapped[str] = mapped_column(String(20), nullable=False)
    description: Mapped[Optional[str]] = mapped_column(String(255), nullable=True)

    user = relationship("User", back_populates="budgets")
    category = relationship("Category", back_populates="budgets")

    def __init__(
        self,
        user_id: int,
        category_id: int,
        amount: float,
        period: str,
        description: Optional[str] = None,
    ) -> None:
        super().__init__()
        self.user_id = user_id
        self.category_id = category_id
        self.amount = amount
        self.period = period
        self.description = description

    def __repr__(self):
        return f"<Budget(id={self.id}, user_id={self.user_id}, category_id={self.category_id}, amount={self.amount}, period='{self.period}', description='{self.description}')>"