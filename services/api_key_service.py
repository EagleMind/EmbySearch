import secrets
from models.api_key import APIKey
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import Depends
from core.database import get_async_db
from sqlalchemy import select
from typing import Optional

class APIKeyService:
    def __init__(self, db: AsyncSession = Depends(get_async_db)):
        self.db = db

    async def create_api_key(self, user_id: int, subscription_type: str) -> APIKey:
        key = secrets.token_hex(16)  # Generate a random API key
        api_key = APIKey(key=key, subscription_type=subscription_type, user_id=user_id)
        self.db.add(api_key)
        await self.db.commit()
        return api_key

    async def get_api_key_details(self, provided_key: str) -> Optional[APIKey]:
        # Fetch the API key from the database
        api_key = await self.db.execute(select(APIKey).where(APIKey.key == provided_key))
        return api_key.scalar_one_or_none()  # Return the APIKey object if found 