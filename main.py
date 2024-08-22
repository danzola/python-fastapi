from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional, List
from httpClientEmail import HttpClientEmail


app = FastAPI()

# Modelo de datos
class Item(BaseModel):
    id: int
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None

# Base de datos simulada
fake_db: List[Item] = []

# Ruta para obtener todos los ítems
@app.get("/items/", response_model=List[Item])
def get_items():
    return fake_db

# Ruta para obtener un ítem por ID
@app.get("/items/{item_id}", response_model=Item)
def get_item(item_id: int):
    item = next((item for item in fake_db if item.id == item_id), None)
    if item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return item

# Ruta para crear un nuevo ítem
@app.post("/items/", response_model=Item)
def create_item(item: Item):
    if any(existing_item.id == item.id for existing_item in fake_db):
        raise HTTPException(status_code=400, detail="Item with this ID already exists")
    fake_db.append(item)
    httpClient = HttpClientEmail()
    httpClient.sendEmail()
    return item

# Ruta para actualizar un ítem por ID
@app.put("/items/{item_id}", response_model=Item)
def update_item(item_id: int, updated_item: Item):
    for index, item in enumerate(fake_db):
        if item.id == item_id:
            fake_db[index] = updated_item
            return updated_item
    raise HTTPException(status_code=404, detail="Item not found")

# Ruta para eliminar un ítem por ID
@app.delete("/items/{item_id}", response_model=Item)
def delete_item(item_id: int):
    for index, item in enumerate(fake_db):
        if item.id == item_id:
            deleted_item = fake_db.pop(index)
            return deleted_item
    raise HTTPException(status_code=404, detail="Item not found")