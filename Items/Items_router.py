from fastapi import APIRouter, Depends
from Items.Item_schema import ItemCreate, ItemResponse, ItemUpdate
from sqlalchemy.orm import Session
from Items import get_session
from typing import List
from Items.Items_controller import Get_all_items, post_item, get_single_item, update_single_item, delete_single_item

router = APIRouter()

@router.get("/items/", response_model=List[ItemResponse])
async def get_items(skip:int = 0, limit: int = 10,db: Session = Depends(get_session)):
    return Get_all_items(skip, limit, db)

@router.post("/items/", response_model=ItemResponse)
async def create_item(item:ItemCreate, db: Session = Depends(get_session)):
    return post_item(item, db)

@router.get("/items/{item_id}", response_model=ItemResponse)
async def read_item(item_id:int, db: Session = Depends(get_session)):
    return get_single_item(item_id, db)

@router.patch("items/{item_id}", response_model=ItemResponse)
async def update_item(item_id:int, item_update:ItemUpdate, db: Session = Depends(get_session)):
    return update_single_item(item_id,item_update, db)

@router.delete("/items/{item_id}", response_model=dict)
async def delete_item(item_id:int, db: Session = Depends(get_session)):
    return delete_single_item(item_id, db)