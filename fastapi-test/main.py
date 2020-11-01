from typing import Optional

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str
    price: float
    is_offer: Optional[bool] = None

@app.get("/")
def hello_world():
    return { "message": "hello world"}

@app.get('/items/{item_id}')
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}

@app.put("/items/{item_id}")
def update_item(item_id: int, itemobject: Item):
    return {
        "item_id": item_id,
        "item_name": itemobject.name,
        "item_price": itemobject.price
    }