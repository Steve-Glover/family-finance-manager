import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, clear_mappers
from sqlalchemy.exc import IntegrityError
from datetime import date


# Import Base from the main models package
from app.models import Base, User, Budget, Transaction, Category
# # Import all models to ensure relationships are registered
# from app.models.user import User
# from app.models.budget import Budget
# from app.models.transaction import Transaction
# from app.models.category import Category

@pytest.fixture(scope="session")
def session():
    """Create a new database session for a test."""
    # Ensure all models are imported before creating tables
    engine = create_engine("sqlite:///:memory:")
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    sess = Session()
    yield sess
    sess.close()
    clear_mappers()


def test_create_user(session):
    """Test creating a user with valid data."""
    user = User(username="alice", email="alice@example.com", password_hash="hashedpw")
    session.add(user)
    session.commit()
    assert user.id is not None
    assert user.username == "alice"
    assert user.email == "alice@example.com"


def test_user_password_not_plaintext(session):
    """Ensure password is stored as a hash, not plaintext."""
    user = User(username="bob", email="bob@example.com", password_hash="hashedpw")
    session.add(user)
    session.commit()
    # There should be no 'password' attribute, only 'password_hash'
    assert not hasattr(user, "password")
    assert hasattr(user, "password_hash")


def test_user_missing_required_field(session):
    """Creating a user without required fields should fail."""
    # Missing username argument: should raise TypeError
    with pytest.raises(TypeError):
        User(email="no_username@example.com", password_hash="hashedpw")
    # Passing None for username: should raise IntegrityError on commit
    user = User(username=None, email="no_username@example.com", password_hash="hashedpw")
    session.add(user)
    with pytest.raises(IntegrityError):
        session.commit()
    session.rollback()


def test_user_relationships(session):
    """Test user relationships with budgets and transactions."""
    user = User(username="carol", email="carol@example.com", password_hash="hashedpw")
    session.add(user)
    # Add a category to satisfy foreign key constraints - note description is required
    category = Category(name="TestCat", description="Test category")
    session.add(category)
    session.commit()
    # Now create budget and transaction with correct foreign keys
    budget = Budget(
        user_id=user.id,
        category_id=category.id,
        amount=1000,
        period="monthly",
        description="Test budget"
    )
    transaction = Transaction(
        user_id=user.id,
        category_id=category.id,
        amount=100,
        date=date(2025, 6, 29),  # Use a proper date object
        type="expense",
        description="Test transaction"
    )
    session.add_all([budget, transaction])
    session.commit()
    # Refresh user relationships
    session.refresh(user)
    assert budget in user.budgets
    assert transaction in user.transactions