from typing import List
from fastapi import APIRouter, Depends, status
from Utils import schemas, database
from sqlalchemy.orm import Session
from Repository import item

router = APIRouter(
    prefix="/item",
    tags=["item"]
)

@router.get('/', response_model = List[schemas.ShowItem], status_code=status.HTTP_200_OK)
def all_items(db : Session = Depends(database.get_db)):
    return item.all_items(db)

@router.get('/{id}', response_model = schemas.ShowItem, status_code = status.HTTP_200_OK)
def get_item_id(id : int, db : Session = Depends(database.get_db)):
    return item.get_item_id(id, db)

@router.post('/', status_code=status.HTTP_201_CREATED)
def add_item(request : schemas.Item, db : Session = Depends(database.get_db)):
    return item.add_item(request, db)

@router.delete("/{id}", status_code=status.HTTP_200_OK)
def delete_item(id : int, db : Session = Depends(database.get_db)):
    return item.delete_item(id, db)

@router.put('/{id}', status_code=status.HTTP_202_ACCEPTED)
def update_item(id : int, request : schemas.Item, db : Session = Depends(database.get_db)):
    return item.update_item(id, request, db)