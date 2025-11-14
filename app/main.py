from fastapi import FastAPI

from app.router.user_router import router as user_router

app = FastAPI()

@app.get("/")
def home():
    return {"message": "API levantada correctamente"}

app.include_router(user_router)

