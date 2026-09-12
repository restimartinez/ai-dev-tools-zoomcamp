import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool

from app.database import Base
from app.main import app


@pytest.fixture
def client() -> TestClient:
    """Provide a fresh TestClient with an isolated in-memory database."""
    engine = create_engine(
        "sqlite://",
        connect_args={"check_same_thread": False},
        poolclass=StaticPool,
    )

    TestingSessionLocal = sessionmaker(
        bind=engine,
        autoflush=False,
        autocommit=False,
    )

    Base.metadata.create_all(bind=engine)

    app.state.testing_session_factory = TestingSessionLocal

    with TestClient(app) as test_client:
        yield test_client

    Base.metadata.drop_all(bind=engine)
    del app.state.testing_session_factory