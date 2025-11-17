from pydantic import BaseModel

class LoginRequest(BaseModel):
    email_or_username: str
    password: str

class SignupRequest(BaseModel):
    username: str
    email: str
    password: str