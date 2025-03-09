from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import SQLAlchemyError
from core.config import settings

from sqlalchemy.ext.asyncio import AsyncSession
from contextlib import asynccontextmanager

# Define the base class for models
Base = declarative_base()

# Create the asynchronous engine
engine = create_async_engine(settings.MAIN_DB_URL, echo=True)

# Create a configured "sessionmaker" class
async_session = sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False
)

# Dependency to get an async session
@asynccontextmanager
async def get_db_session() -> AsyncSession:
    async with async_session() as session:
        try:
            yield session
        except SQLAlchemyError as e:
            print(f"Session error: {e}")
            raise

async def get_async_db() -> AsyncSession:
    async with async_session() as session:
        yield session

# Function to initialize the database
async def init_db():
    try:
        async with engine.begin() as conn:
            print("Creating tables...")
            await conn.run_sync(Base.metadata.create_all)  # This will create tables for all models
            print("Tables created successfully.")
            created_tables = Base.metadata.tables.keys()
            if not created_tables:
                print("No tables were created.")
            else:
                for table in created_tables:
                    print(f"Created table: {table}")
                    print(f"Query to check the table: SELECT * FROM {table};")
    except SQLAlchemyError as e:
        print(f"Database initialization error: {e}")
        raise
