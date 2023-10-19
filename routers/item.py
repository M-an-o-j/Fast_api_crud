from fastapi import APIRouter, HTTPException, Depends
from database.models import Item
from schema.item import ItemCreate, ItemResponse, ItemUpdate
from sqlalchemy.orm import Session
from database import get_session
from typing import List
from fastapi import HTTPException

router = APIRouter()

@router.get("/items/", response_model=List[ItemResponse])
async def get_items(skip:int = 0, limit: int = 10,db: Session = Depends(get_session)):
    try:
        items = db.query(Item).offset(skip).limit(limit).all()
    except Exception as e:
        raise HTTPException(status_code=500, detail="Tnternal server error")
    return items

@router.post("/items/", response_model=ItemResponse)
async def create_item(item:ItemCreate, db: Session = Depends(get_session)):
    try:
        db_item = Item(**item.dict())
        db.add(db_item)
        db.commit()
        db.refresh(db_item)
    except Exception as e:
        raise HTTPException(status_code=500, detail="Internal server error")
    return db_item

@router.get("/items/{item_id}", response_model=ItemResponse)
async def read_item(item_id:int, db: Session = Depends(get_session)):
    try:
        db_item = db.query(Item).filter(Item.id == item_id).first()
        if db_item is None:
            raise HTTPException(status_code=404, detail="Its not found")
    except Exception as e:
        raise HTTPException(status_code=500, detail="Internal server error")
    return db_item

@router.patch("items/{item_id}", response_model=ItemResponse)
async def update_item(item_id:int, item_update:ItemUpdate, db: Session = Depends(get_session)):
    try:
        db_item = db.query(Item).filter(Item.id == item_id).first()
        if db_item is None:
            raise HTTPException(status_code= 404, detail="Item not found")
        if item_update.name:
            db_item.name = item_update.name
        if item_update.description:
            db_item.description = item_update.description
        if item_update.price:
            db_item.price = item_update.price
        if item_update.tax:
            db_item.tax = item_update.tax
        

        db.commit()
        db.refresh(db_item)
    except Exception as e:
        raise HTTPException(status_code=500, detail="Internal server error")
    return db_item

@router.delete("/items/{item_id}", response_model=dict)
async def delete_item(item_id:int, db: Session = Depends(get_session)):
    try:
        db_item = db.query(Item).filter(Item.id == item_id).first()
        if db_item is None:
            raise HTTPException(status_code=404, detail="Its not found")
        
        db.delete(db_item)
        db.commit()
    except Exception as e:
        raise HTTPException(status_code=500, detail="Internal server error")
    return {"message" : f"Item {item_id} has been deleted"}