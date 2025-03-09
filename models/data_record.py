from sqlmodel import SQLModel, Field, Relationship
from sqlalchemy import Column, JSON
from typing import Optional, Dict, Any, List
from datetime import datetime
from models.user import User  
class DataRecord(SQLModel, table=True):  # Ensure table=True to map it to a database table
    id: str = Field(primary_key=True)
    data: List[Dict[str, Any]] = Field(sa_column=Column(JSON)) 
    collection: str = Field(default="default")
    created_at: datetime = Field(default_factory=datetime.now)
    
    user_id: Optional[int] = Field(default=None, foreign_key="user.id")  
    user: Optional[User] = Relationship(back_populates="data_records") 

