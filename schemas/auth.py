from typing import List,Optional,Any,Literal
from pydantic import BaseModel,Field,ConfigDict,EmailStr
import uuid


class RegisterRequest(BaseModel):
    organization_name : str = Field(min_length=2,max_length=35)
    organization_slug : str = Field(min_length=2,max_length=135)
    full_name : str = Field(description="Nname of the user")
    email : EmailStr
    password : str = Field(min_length=8,max_length=16)

class LoginRequest(BaseModel):
    organization_slug : str = Field(min_length=2,max_length=135)
    email : EmailStr 
    password : str = Field(min_length=8,max_length=16)

class UserResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id : uuid.UUID = Field(description="user_id")
    organization_id : uuid.UUID = Field(description="organization_id")
    full_name : str
    email : str
    role : Literal["owner","admin","member"]
    is_active : bool = Field("Status of account")

class TokenResponse(BaseModel):
    access_token : str 
    token_type : str = "bearer"
    expires_in : int
    user : UserResponse



