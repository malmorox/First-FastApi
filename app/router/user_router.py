from fastapi import APIRouter, HTTPException
from models.auth import LoginRequest, SignupRequest
from utils.json_utils import load_json, save_json

router = APIRouter(prefix="/auth", tags=["auth"])

@router.post("/signup")
def signup(data: SignupRequest):
    db = load_json("users.json")
    users = db["users"]

    for u in users:
        if u["username"] == data.username:
            raise HTTPException(400, "El username ya existe")
        if u["email"] == data.email:
            raise HTTPException(400, "El email ya está registrado")

    new_user = {
        "id": str(len(users) + 1),
        "username": data.username,
        "email": data.email,
        "password": data.password
    }

    users.append(new_user)
    save_json(db)

    return {
        "success": True,
        "message": "Usuario creado correctamente",
        "user": new_user
    }


@router.post("/login")
def login(data: LoginRequest):
    db = load_json("users.json")
    users = db["users"]

    for u in users:
        if (u["username"] == data.email_or_username or 
            u["email"] == data.email_or_username) and u["password"] == data.password:
            
            return {
                "success": True,
                "message": "Login correcto",
                "user": u
            }

    raise HTTPException(401, "Credenciales incorrectas")


@router.get("/users")
def get_users():
    db = load_json("users.json")
    return {"users": db["users"]}


@router.get("/users/{user_id}")
def get_user(user_id: str):
    db = load_json("users.json")
    users = db["users"]

    for u in users:
        if u["id"] == user_id:
            return {"user": u}

    raise HTTPException(404, "Usuario no encontrado")


@router.put("/users/{user_id}")
def update_user(user_id: str, data: SignupRequest):
    db = load_json("users.json")
    users = db["users"]

    for u in users:
        if u["id"] == user_id:
            u["username"] = data.username
            u["email"] = data.email
            u["password"] = data.password
            save_json(db)
            return {"success": True, "message": "Usuario actualizado correctamente", "user": u}

    raise HTTPException(404, "Usuario no encontrado")


@router.delete("/users/{user_id}")
def delete_user(user_id: str):
    db = load_json("users.json")
    users = db["users"]

    for u in users:
        if u["id"] == user_id:
            users.remove(u)
            save_json(db)
            return {"success": True, "message": "Usuario eliminado correctamente"}

    raise HTTPException(404, "Usuario no encontrado")