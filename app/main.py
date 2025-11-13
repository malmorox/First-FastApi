from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

class LoginRequest(BaseModel):
    username: str
    password: str

FAKE_USER = {
    "username": "test",
    "password": "1234"
}


@app.get("/")
def root():
    return {"message": "API levantada"}


@app.post("/login")
def login(data: LoginRequest):
    if data.username == FAKE_USER["username"] and data.password == FAKE_USER["password"]:
        
        return {
            "success": True,
            "message": "Login correcto"
        }
    else:
        raise HTTPException(
            status_code=401,
            detail="Credenciales incorrectas"
        )
