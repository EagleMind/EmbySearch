from sqlmodel import SQLModel, Field, Relationship
from typing import List
from datetime import datetime, timezone

class User(SQLModel, table=True):
    id: int = Field(primary_key=True)
    username: str = Field(index=True)
    email: str = Field(index=True)
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    
    # Define a relationship to DataRecord
    data_records: List["DataRecord"] = Relationship(back_populates="user")  # Ensure correct reference 