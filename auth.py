from fastapi import HTTPException, Security
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
import os

API_KEY = os.getenv("API_KEY", "Ran's-BE-Project")

security = HTTPBearer()

def verify_api_key(credentials: HTTPAuthorizationCredentials = Security(security)) -> str:
    if credentials.credentials != API_KEY:
        raise HTTPException(
            status_code=401,
            detail="Invalid API key"
        )
    return credentials.credentials
