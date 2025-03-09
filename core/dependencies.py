from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from core.security import verify_jwt_token

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

async def get_current_user(token: str = Depends(oauth2_scheme)):
    user_id = verify_jwt_token(token)
    if user_id is None:
        raise HTTPException(status_code=401, detail="Invalid token")
    return user_id 