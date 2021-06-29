from fastapi import FastAPI, Depends, status, HTTPException
from sqlalchemy.sql.functions import mode
from sqlalchemy.sql.sqltypes import Float
from Shop import schemas, models
from Shop.database import engine, SessionLocal
from sqlalchemy.orm import Session
from typing import List

app = FastAPI()

models.Base.metadata.create_all(engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close

@app.get('/item', response_model = List[schemas.Item], status_code=status.HTTP_200_OK)
async def all_items(db : Session = Depends(get_db)):
    items = db.query(models.Item).all()
    return items

@app.get('/item/{id}', response_model = schemas.Item, status_code = status.HTTP_200_OK)
async def get_item_id(id : int, db : Session = Depends(get_db)):
    item = db.query(models.Item).filter(models.Item.id == id).first()
    if not item: 
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Cannot find items with id = {id}")
    return item

@app.post('/item', status_code=status.HTTP_201_CREATED)
async def add_item(request : schemas.Item, db : Session = Depends(get_db)):
    item = models.Item(name = request.name, price = request.price)
    db.add(item)
    db.commit()
    db.refresh(item)
    return item

@app.delete("/item/{id}", status_code=status.HTTP_200_OK)
async def delete_item(id : int, db : Session = Depends(get_db)):
    ammount = db.query(models.Item).filter(models.Item.id == id).delete(synchronize_session=False)
    if ammount != 1:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    db.commit()

@app.put('/item/{id}', status_code=status.HTTP_202_ACCEPTED)
async def update_item(id : int, request : schemas.Item, db : Session = Depends(get_db)):
    item = db.query(models.Item).filter(models.Item.id == id)
    if not item.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    item.update(request)
    db.commit()