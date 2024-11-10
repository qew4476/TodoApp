# To check whether the request is authorized or not

from fastapi import HTTPException, Security
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

class JWTBearer(HTTPBearer):
    def __init__(self, auto_error: bool = True):
        super(JWTBearer, self).__init__(auto_error=auto_error)

    async def __call__(self, credentials: HTTPAuthorizationCredentials = Security(HTTPAuthorizationCredentials)):
        if credentials.scheme.lower() != "bearer":
            raise HTTPException(status_code=403, detail="Invalid authentication scheme")
        if not credentials.credentials:
            raise HTTPException(status_code=403, detail="Invalid token credentials")
        return credentials.credentials