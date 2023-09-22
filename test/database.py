from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "sqlite:///./sql_app.db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


users_db = [
    {
        "name": "John",
        "surname": "Doe",
        "email": "john.doe@example.com",
        "eth_address": "0x0914B7665920386a9F05a53e83d1c999B25Eedb5",
        "password": "password123",
    },
    {
        "name": "Alice",
        "surname": "Smith",
        "email": "alice.smith@example.com",
        "eth_address": "0x0914B7665920386a9F05a53e83d1c999B25Eedb5",
        "password": "password123",
    },
    {
        "name": "Bob",
        "surname": "Johnson",
        "email": "bob.johnson@example.com",
        "eth_address": "0x0914B7665920386a9F05a53e83d1c999B25Eedb5",
        "password": "password123",
    },
]
