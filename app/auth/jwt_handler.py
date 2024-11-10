#This file is used to handle the JWT token generation and verification
#That is, signing, encoding, decoding and returning JWTs

import time             #every job has its expired time
import jwt              #encoding&decoding token strings
from decouple import config         #organizing setting, such as changing setting without the need to redeploy app

JWT_SECRET = config("SECRET")
JWT_ALGORITHM = config("ALGORITHM")

#It returns the generated Tokens (JWTs)
def token_response(token:str):
    return{
        "access token" : token

    }

#sign the JWT string
def signJWT(user_id:str):
    payload = {
        "user_id": user_id,
        "expiry": time.time() + 600
    }
    token = jwt.encode(payload,JWT_SECRET,algorithm=JWT_ALGORITHM)
    return token_response(token)

def decodeJWT(token:str):
    try:
        decode_token = jwt.decode(token,JWT_SECRET,algorithms=JWT_ALGORITHM)
        if decode_token['expiry'] >= time.time():
            return decode_token
        else:
            return None
    except:
        return{}

# Everybody can decode token easily(BASE64), but only the JWT website can verify its authenticity with the JWT secret