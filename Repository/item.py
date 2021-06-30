from sqlalchemy.orm import Session
from Utils import models, schemas
from fastapi import HTTPException,status


def all_items(db : Session):
    items = db.query(models.Item).all()
    return items

def get_item_id(id : int, db : Session):
    item = db.query(models.Item).filter(models.Item.id == id).first()
    if not item: 
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Cannot find items with id = {id}")
    return item

def add_item(request : schemas.Item, db : Session):
    item = models.Item(name = request.name, price = request.price)
    db.add(item)
    db.commit()
    db.refresh(item)
    return item

def delete_item(id : int, db : Session):
    item = db.query(models.Item).filter(models.Item.id == id)
    if item != 1:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    item.delete(synchronize_session=False)
    db.commit()
    return "Done!"

def update_item(id : int, request : schemas.Item, db : Session):
    item = db.query(models.Item).filter(models.Item.id == id)
    if not item.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    item.update(request)
    db.commit()
    return "Done!"