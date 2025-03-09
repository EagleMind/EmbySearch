from fastapi import APIRouter, Depends, HTTPException
from models.data_record import DataRecord
from services.data_service import DataService
from core.database import get_async_db  # Import the async database session
from sqlalchemy.ext.asyncio import AsyncSession
from services.api_key_service import APIKeyService  # Import the APIKeyService

router = APIRouter()

@router.post("/data")
async def create_data_record(
    record: DataRecord,
    api_key: str,  # Expecting API key as a parameter
    db: AsyncSession = Depends(get_async_db)  # Get the database session
):
    api_key_service = APIKeyService(db)
    is_valid = await api_key_service.validate_api_key(api_key)
    
    if not is_valid:
        raise HTTPException(status_code=403, detail="Invalid API key")

    # Fetch the API key details to check subscription type
    api_key_details = await api_key_service.get_api_key_details(api_key)
    
    if api_key_details.subscription_type not in ["Basic", "Premium"]:
        raise HTTPException(status_code=403, detail="Access denied for this resource")

    service = DataService(db)  # Pass the session to the service
    await service.create_record(record)
    return {"status": "success"}
