from typing import Generator

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

from resume_filter_API.Configuration import mysql_port, mysql_user, mysql_database, mysql_server, mysql_password

# Create SQLAlchemy engine and session
database_url = f"mysql+mysqlconnector://{mysql_user}:{mysql_password}@{mysql_server}:{mysql_port}/{mysql_database}"
engine = create_engine(database_url, echo=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Create all tables
Base.metadata.create_all(bind=engine)
# Check connection
try:
    connection = engine.connect()
    print("Database connected successfully!")
except Exception as e:
    print(f"Failed to connect to the database: {e}")


# Dependency
def get_db() -> Generator:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
