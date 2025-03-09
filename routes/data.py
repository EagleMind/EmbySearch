from fastapi import APIRouter, Depends
from models.data_record import DataRecord
from services.data_service import DataService
from core.database import get_async_db  # Import the async database session
from sqlalchemy.ext.asyncio import AsyncSession

router = APIRouter()

@router.post("/data")
async def create_data_record(
    record: DataRecord,
    db: AsyncSession = Depends(get_async_db)  # Get the database session
):
    service = DataService(db)  # Pass the session to the service
    await service.create_record(record)
    return {"status": "success"}
