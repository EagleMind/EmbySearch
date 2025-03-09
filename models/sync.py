from pydantic import BaseModel
from typing import Dict, Any, Optional

class SyncDataRecordRequest(BaseModel):
    event: str
    id: str
    data: Dict[str, Any]
    collection: str
    user_id: Optional[int] = None  # Optional field 