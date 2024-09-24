from pydantic import BaseModel


class UserCreate(BaseModel):
    username: str
    email: str
    password: str


class UserLogin(BaseModel):
    username: str
    password: str


class UserFileUpload(BaseModel):
    title: str
    file: str
    user_id: int


class CreateQuestion(BaseModel):
    question: str
