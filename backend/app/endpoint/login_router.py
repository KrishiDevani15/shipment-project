from fastapi import APIRouter
login_router = APIRouter()

@login_router.get("/")
def hello():
    return {"message": "Hello from login_router!"}