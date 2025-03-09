from fastapi import FastAPI
from routes import data, search, sync, auth
import bcrypt

app = FastAPI()

# Register routes
app.include_router(data.router, prefix="/api/v1")
app.include_router(search.router, prefix="/api/v1")
app.include_router(sync.router, prefix="/api/v1")
app.include_router(auth.router, prefix="/api/v1")
