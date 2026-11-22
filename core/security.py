from datetime import datetime,timedelta,timezone
from pwdlib import PasswordHash
import jwt
import uuid
from core import get_config

settings = get_config()

hash = PasswordHash.recommended()

def hash_password(password : str):
    return hash.hash(password=password)

def verify_password(plain_password : str,
                    hash_password : str):
    return hash.verify(
        plain_password,
        hash_password
    )

def create_access_token(user_id:str,
                        organization_id:str):
    current_time = datetime.now(timezone.utc)
    expiry_time = current_time + timedelta(minutes=settings.access_token_expiry_minutes)

    payload = {
        "sub": f"{user_id}",
        "org":f"{organization_id}",
        "jti":f"{uuid.uuid4()}",
        "iss":settings.jwt_issuer,
        "aud":settings.jwt_author,
        "iat":current_time,
        "exp":expiry_time
    }

    return jwt.encode(payload=payload,
                      algorithm=settings.jwt_algorithm,
                      key=settings.jwt_secret_key.get_secret_value(),
                      issuer=settings.jwt_issuer,
                      author=settings.jwt_author)