# Pydantic model

from pydantic import BaseModel
from datetime import *

class UserBase(BaseModel):
    # password: str
    username: str
    email: str
    username: str
    # created_at: datetime
    # updated_at: datetime
    profile_pic: str
    activated: bool
    phone_number: str
    fullname: str
    

class UserCreate(UserBase):
    password: str

class UserById(UserBase):
    id: int
    
    class Config:
        from_attributes = True

class UserByName(UserBase):
    username: str
    
    class Config:
        from_attributes = True

class UserLogin(BaseModel):
    username: str
    password: str

class UserUpdate:
    pass


