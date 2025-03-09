from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from sqlalchemy.ext.asyncio import AsyncSession
from core.database import get_async_db
from models.user import User
from core.security import hash_password, verify_password, create_jwt_token
from fastapi import Depends
from sqlalchemy import select

router = APIRouter()

class UserCreate(BaseModel):
    username: str
    email: str
    password: str

@router.post("/register")
async def register_user(user: UserCreate, db: AsyncSession = Depends(get_async_db)):
    hashed_password = hash_password(user.password)
    new_user = User(username=user.username, email=user.email, password=hashed_password)
    db.add(new_user)
    await db.commit()
    return {"status": "success", "message": "User registered successfully"}

class UserLogin(BaseModel):
    username: str
    password: str

@router.post("/login")
async def login(user: UserLogin, db: AsyncSession = Depends(get_async_db)):
    db_user = await db.execute(select(User).where(User.username == user.username))
    user_record = db_user.scalar_one_or_none()
    
    if not user_record or not verify_password(user.password, user_record.password):
        raise HTTPException(status_code=401, detail="Invalid credentials")
    
    token = create_jwt_token(user_record.id)
    return {"access_token": token, "token_type": "bearer"} 