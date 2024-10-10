from app.models.item_model import Item
from app.services.email_service import EmailService
from fastapi import HTTPException
from typing import List

fake_items_db = []

def create_item(item: Item) -> Item:
    if any(existing_item.id == item.id for existing_item in fake_items_db):
            raise HTTPException(status_code=400, detail="Item with this ID already exists")
    fake_items_db.append(item)
    email_service = EmailService()
    email_service.send_email()
    return item

def get_item(item_id: int) -> Item:
    item = next((item for item in fake_items_db if item.id == item_id), None)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    return item    

def get_items() -> List[Item]:
    return fake_items_db

def update_item(item_id: int, updated_item: Item) -> Item:
     for index, item in enumerate(fake_items_db):
        if item.id == item_id:
            fake_items_db[index] = updated_item
            return updated_item
        raise HTTPException(status_code=404, detail="Item not found")
     
def delete_item(item_id: int) -> Item:
    for index, item in enumerate(fake_items_db):
        if item.id == item_id:
            deleted_item = fake_items_db.pop(index)
            return deleted_item
    raise HTTPException(status_code=404, detail="Item not found")     