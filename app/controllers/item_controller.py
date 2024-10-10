from fastapi import APIRouter
from app.models.item_model import Item
import app.services.item_service as item_service
from typing import List

router = APIRouter(
    prefix="/items",
    tags=["items"],
)

@router.get("/", response_model=List[Item])
def get_items():
    return item_service.get_items()

@router.post("/", response_model=Item)
def create_new_item(item: Item):    
    return item_service.create_item(item)

@router.get("/{item_id}", response_model=Item)
def read_item(item_id: int):
    return item_service.get_item(item_id)

@router.put("/{item_id}", response_model=Item)
def update_item(item_id: int, updated_item: Item):
    return item_service.update_item(item_id,updated_item)

@router.delete("/{item_id}", response_model=Item)
def delete_item(item_id: int):
    return item_service.delete_item(item_id)