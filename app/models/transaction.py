from sqlalchemy import Integer, Float, String, Date, ForeignKey
from sqlalchemy.orm import relationship, Mapped, mapped_column
from . import Base
from datetime import date as date_class
from typing import Union

class Transaction(Base):
    """
    Represents an income or expense transaction in the Family Finance Manager system.

    :param id: Unique identifier for the transaction.
    :param user_id: Foreign key referencing the user.
    :param category_id: Foreign key referencing the category.
    :param amount: The transaction amount.
    :param date: The date of the transaction.
    :param description: Optional description of the transaction.
    :param type: The type of transaction ("income" or "expense").
    """
    __tablename__ = "transaction"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    user_id: Mapped[int] = mapped_column(Integer, ForeignKey("user.id"), nullable=False)
    category_id: Mapped[int] = mapped_column(Integer, ForeignKey("category.id"), nullable=False)
    amount: Mapped[float] = mapped_column(Float, nullable=False)
    date: Mapped[date_class] = mapped_column(Date, nullable=False)
    description: Mapped[str] = mapped_column(String(255), nullable=False)
    type: Mapped[str] = mapped_column(String(16), nullable=False)  # "income" or "expense"

    user = relationship("User", back_populates="transactions")
    category = relationship("Category", back_populates="transactions")

    def __init__(
        self,
        user_id: int,
        category_id: int,
        amount: float,
        date: Union[str, date_class],
        type: str,
        description: str,
    ) -> None:
        """
        Initializes a Transaction instance.

        :param user_id: ID of the user associated with the transaction.
        :param category_id: ID of the category associated with the transaction.
        :param amount: The transaction amount.
        :param date: The date of the transaction as a string in 'YYYY-MM-DD' format or date object.
        :param type: The type of transaction ("income" or "expense").
        :param description: Description of the transaction.
        """
        super().__init__()
        self.user_id = user_id
        self.category_id = category_id
        self.amount = amount
        # Convert string date to datetime.date object
        if isinstance(date, str):
            self.date = date_class.fromisoformat(date)
        else:
            self.date = date
        self.type = type
        self.description = description

    def __repr__(self):
        return (
            f"<Transaction(id={self.id}, user_id={self.user_id}, category_id={self.category_id}, "
            f"amount={self.amount}, date={self.date}, description={self.description}, type={self.type})>"
        )