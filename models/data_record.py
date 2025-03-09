from sqlmodel import SQLModel, Field, Relationship
from sqlalchemy import Column, JSON
from typing import Optional, Dict, Any, List
from datetime import datetime
from models.user import User  # Ensure User is imported here

class DataRecord(SQLModel, table=True):  # Ensure table=True to map it to a database table
    id: str = Field(primary_key=True)
    data: List[Dict[str, Any]] = Field(sa_column=Column(JSON))  # Changed to allow an array of JSON objects
    collection: str = Field(default="default")
    created_at: datetime = Field(default_factory=datetime.now)  # Changed to offset-naive
    
    # Define a relationship to the User model using a string reference
    user_id: Optional[int] = Field(default=None, foreign_key="user.id")  # Assuming User has an 'id' field
    user: Optional[User] = Relationship(back_populates="data_records")  # Relationship back to User

