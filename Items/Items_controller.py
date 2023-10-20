from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from Items.Items_models import Item

def Get_all_items(skip , limit, db):
    try:
        print("Hii")
        items = db.query(Item).all()
        print(items)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"{e}")
    return items

def post_item(item, db):
    try:
        db_item = Item(**item.dict())
        db.add(db_item)
        db.commit()
        db.refresh(db_item)
    except Exception as e:
        raise HTTPException(status_code=500, detail="Internal server error")
    return db_item

def get_single_item(item_id, db):
    try:
        db_item = db.query(Item).filter(Item.id == item_id).first()
        if db_item is None:
            raise HTTPException(status_code=404, detail="Its not found")
    except Exception as e:
        raise HTTPException(status_code=500, detail="Internal server error")
    return db_item

def update_single_item(item_id,item_update, db):
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
        raise HTTPException(status_code=500, detail=f"{e}")
    return db_item

def delete_single_item(item_id, db):
    try:
        db_item = db.query(Item).filter(Item.id == item_id).first()
        if db_item is None:
            raise HTTPException(status_code=404, detail="Its not found")
        
        db.delete(db_item)
        db.commit()
    except Exception as e:
        raise HTTPException(status_code=500, detail={
            "message": "Internal Server error",
            "error": e
        }, )
    return {"message" : f"Item {item_id} has been deleted"}