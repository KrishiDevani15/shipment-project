from fastapi import FastAPI
from app.endpoint.login_router import login_router

app = FastAPI()
app.include_router(login_router)
