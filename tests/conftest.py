import pytest
from fastapi.testclient import TestClient
from main import app
from database import Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Use an in-memory SQLite database for testing
SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

@pytest.fixture
def db_session():
    Base.metadata.create_all(bind=engine)  # Create test tables
    db = TestingSessionLocal()
    yield db
    db.close()
    Base.metadata.drop_all(bind=engine)  # Clean up after tests

@pytest.fixture
def client():
    return TestClient(app)