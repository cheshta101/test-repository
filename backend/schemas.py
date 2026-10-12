##schemas.py   → API request/response

# from pydantic import BaseModel


# class UserCreate(BaseModel):  ##then UserCreate is your Pydantic schema for validating incoming user data.
#     ## class UserResponse(BaseModel):  it can be UserResponse for update, so it changed as per req and we will use it in main.py as we used the UserCreate
#     name: str
#     email: str
#     age: int



# from pydantic import BaseModel


# class UserCreate(BaseModel):
#     name: str
#     email: str
#     age: int    

##postgre
# from pydantic import BaseModel


# class UserCreate(BaseModel):
#     name: str
#     email: str
#     age: int        


# # PUT - Update complete user
# class UserUpdate(BaseModel):
#     name: str
#     email: str
#     age: int


# # PATCH - Update only selected fields
# class UserPatch(BaseModel):
#     name: str | None = None
#     email: str | None = None
#     age: int | None = None
##postgre

##mongodb 

from pydantic import BaseModel, EmailStr
from typing import Optional


class UserCreate(BaseModel):
    name: str
    email: EmailStr
    age: Optional[int] = None
    password: str              # new


class UserUpdate(BaseModel):
    name: str
    email: EmailStr
    age: Optional[int] = None


class UserPatch(BaseModel):
    name: Optional[str] = None
    email: Optional[EmailStr] = None
    age: Optional[int] = None


# For returning user data
class UserResponse(BaseModel):
    id: str
    name: str
    email: EmailStr
    age: Optional[int] = None
##mongodb    


