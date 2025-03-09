from sqlmodel import SQLModel, Field, Relationship
from typing import List
from datetime import datetime
import uuid  # Import uuid for generating unique identifiers

class User(SQLModel, table=True):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()), primary_key=True)  # Change to str and use UUID
    username: str = Field(index=True)
    email: str = Field(index=True)
    password: str  # Add password field
    created_at: datetime = Field(default_factory=datetime.now)  # Use naive datetime
    
    # Define a relationship to DataRecord
    data_records: List["DataRecord"] = Relationship(back_populates="user")  # Ensure correct reference 
    api_keys: List["APIKey"] = Relationship(back_populates="user")  # Relationship to APIKey 