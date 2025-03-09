from models.data_record import DataRecord
from services.chroma import ChromaService
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import Depends
from core.database import get_async_db  # Ensure this function provides an AsyncSession
from sqlalchemy import select
from typing import Optional

class DataService:
    def __init__(self, db: AsyncSession = Depends(get_async_db)):
        self.db = db
        self.chroma = ChromaService()

    async def create_record(self, record: DataRecord):
        # Check if the record already exists
        existing_record = await self.db.get(DataRecord, record.id)
        if existing_record:
            return existing_record  # Return the existing record to avoid duplication

        # PostgreSQL operations
        db_record = DataRecord(**record.dict())
        self.db.add(db_record)
        await self.db.commit()

        # Chroma operations
        await self.chroma.add_document(
            document_id=record.id,
            data=record.data,
            collection=record.collection
        )
        
        return db_record

    async def handle_webhook(self, payload: dict):
        # Implement CRUD operations based on webhook events
        pass

    async def get_record_by_index(self, external_id: str) -> Optional[DataRecord]:
        return await self.db.execute(select(DataRecord).where(DataRecord.externalid == external_id)).scalar_one_or_none()  # Fetch record by index
