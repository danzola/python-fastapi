from fastapi import FastAPI
from app.controllers import item_controller,callback_controller

app = FastAPI()
app.include_router(item_controller.router)
app.include_router(callback_controller.router)