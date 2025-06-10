from pydantic import BaseModel, EmailStr
from datetime import date


class UserResponse(BaseModel):
    id: int
    first_name: str
    last_name: str
    email: EmailStr
    birthday: date

    class Config:
        from_attributes = True

class UserUpdate(BaseModel):
    first_name: str = None
    last_name: str = None
    email: EmailStr = None
    birthday: date = None

    class Config:
        from_attributes = True