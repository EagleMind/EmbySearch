from fastapi import APIRouter, Depends
from models.data_record import DataRecord
from models.sync import SyncDataRecordRequest 
from services.data_service import DataService
from core.database import get_async_db
from sqlalchemy.ext.asyncio import AsyncSession

router = APIRouter()

@router.post("/sync")
async def sync_data_record(
    request: SyncDataRecordRequest, 
    db: AsyncSession = Depends(get_async_db)
):
    if request.event != "update":
        return {"status": "error", "message": "Invalid event type. Only 'update' is allowed."}

    # Create a DataRecord instance from the request data
    record = DataRecord(
        id=request.id,
        data=request.data,
        collection=request.collection,
        user_id=request.user_id
    )

    service = DataService(db) 
    updated_record = await service.create_record(record) 
    return {"status": "success", "record": updated_record}