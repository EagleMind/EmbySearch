from sqlmodel import SQLModel, Field, Relationship
from typing import Optional
from models.user import User 

class APIKey(SQLModel, table=True):
    id: int = Field(primary_key=True)
    key: str = Field(index=True, unique=True) 
    subscription_type: str 
    user_id: int = Field(foreign_key="user.id") 
    user: Optional[User] = Relationship(back_populates="api_keys") 