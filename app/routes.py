from fastapi import APIRouter, HTTPException
from app.models import Item

router = APIRouter()

# GET endpoint
@router.get("/")
def read_root():
    return {"message": "Hello, Unified AI Service!"}

# POST endpoint
@router.post("/items/")
def create_item(item: Item):
    try:
        return {"message": "Item created successfully", "item": item}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
