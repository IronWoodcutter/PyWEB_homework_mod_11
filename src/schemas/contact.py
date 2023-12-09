from datetime import date

from pydantic import BaseModel, EmailStr, Field


class ContactSchema(BaseModel):
    firstname: str = Field(min_length=3, max_length=50)
    lastname: str = Field(min_length=3, max_length=50)
    email: EmailStr
    phone: str = Field(min_length=3, max_length=30)
    birthday: date = Field(format="%Y-%m-%d")
    additional_data: str = Field(min_length=3, max_length=250)


class ContactResponse(BaseModel):
    id: int = 1
    firstname: str
    lastname: str
    email: EmailStr
    phone: str
    birthday: date
    additional_data: str

    class Config:
        from_attributes = True
