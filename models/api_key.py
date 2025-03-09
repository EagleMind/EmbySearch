from sqlmodel import SQLModel, Field, Relationship
from typing import Optional
from models.user import User  # Ensure User is imported here

class APIKey(SQLModel, table=True):
    id: int = Field(primary_key=True)
    key: str = Field(index=True, unique=True)  # Unique API key
    subscription_type: str  # Subscription type attribute
    user_id: int = Field(foreign_key="user.id")  # Foreign key to User
    user: Optional[User] = Relationship(back_populates="api_keys")  # Relationship back to User 