from sqlalchemy.orm import declarative_base

Base = declarative_base()

# Import all models to register them with SQLAlchemy
from .user import User
from .category import Category
from .budget import Budget
from .transaction import Transaction

__all__ = ["Base", "User", "Category", "Budget", "Transaction"]