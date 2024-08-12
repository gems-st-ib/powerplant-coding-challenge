from fastapi import FastAPI
from app.app.controller.main_controller import router

app = FastAPI()
app.include_router(router, prefix="/api")
