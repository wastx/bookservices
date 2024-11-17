from pydantic import BaseModel, Field
import uuid
from datetime import datetime
from src.books.schemas import Book
from src.reviews.schemas import ReviewModel


class UserCreateModel(BaseModel):
    first_name: str = Field(max_length=25)
    last_name: str = Field(max_length=25)
    username: str = Field(max_length=26)
    email: str = Field(max_length=40)
    password: str = Field(min_length=6)


class UserModel(BaseModel):
    uid: uuid.UUID
    username: str
    email: str
    first_name: str
    last_name: str
    is_verified: bool
    password_hash: str = Field(exclude=True)
    created_at: datetime
    update_at: datetime


class UserBooksModel(UserModel):
    books: list[Book]
    reviews: list[ReviewModel]


class UserLoginModel(BaseModel):
    email: str = Field(max_length=40)
    password: str = Field(min_length=6)


class EmailModel(BaseModel):
    addresses: list[str]


class PasswordResetRequestModel(BaseModel):
    email: str


class PasswordResetConfirmModel(BaseModel):
    new_password: str
    confirm_new_password: str
