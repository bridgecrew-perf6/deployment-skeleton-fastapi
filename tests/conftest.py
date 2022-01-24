import pytest
from fastapi.testclient import TestClient
from sqlalchemy.orm import sessionmaker
from tenacity import retry, stop_after_delay

from fastapi_sandbox.database import engine
from fastapi_sandbox.main import app
from fastapi_sandbox.models import Base


@retry(stop=stop_after_delay(10))
def wait_for_postgres_to_come_up(engine):
    return engine.connect()


@pytest.fixture(scope="session")
def postgres_db():
    Base.metadata.create_all(engine)
    return engine


@pytest.fixture
def postgres_session_factory(postgres_db):
    yield sessionmaker(bind=postgres_db)


@pytest.fixture
def postgres_session(postgres_session_factory):
    session = postgres_session_factory()
    yield session
    session.close()


@pytest.fixture(autouse=True)
def clear_db(postgres_session):
    for table in reversed(Base.metadata.sorted_tables):
        postgres_session.execute(table.delete())
    postgres_session.commit()


@pytest.fixture(scope="class")
def client():
    yield TestClient(app)
