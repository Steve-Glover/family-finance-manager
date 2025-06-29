from sqlalchemy import Integer, String
from sqlalchemy.orm import relationship, declarative_base, Mapped, mapped_column

Base = declarative_base()

class User(Base):
    """
    Represents a user account in the Family Finance Manager system.

    :param id: Unique identifier for the user.
    :param username: Unique username for the user.
    :param email: Unique email address for the user.
    :param password_hash: Hashed password for authentication.
    """
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    username: Mapped[str] = mapped_column(String(64), unique=True, nullable=False)
    email: Mapped[str] = mapped_column(String(120), unique=True, nullable=False)
    password_hash: Mapped[str] = mapped_column(String(128), nullable=False)

    budgets = relationship("Budget", back_populates="user", cascade="all, delete-orphan")
    transactions = relationship("Transaction", back_populates="user", cascade="all, delete-orphan")

    def __repr__(self) -> str:
        return f"<User(username='{self.username}', email='{self.email}')>"