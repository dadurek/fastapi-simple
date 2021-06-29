from fastapi import FastAPI, Depends
from Shop import schemas, models
from Shop.database import engine, SessionLocal
from sqlalchemy.orm import Session, session

app = FastAPI()

models.Base.metadata.create_all(engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close

@app.get('/')
async def index():
    return {'data':'simple example'}

@app.get('/item')
async def all_items(db : Session = Depends(get_db)):
    items = db.query(models.Item).all()
    return items

@app.get('/item/{id}')
async def get_item_id(id : int, db : Session = Depends(get_db)):
    item = db.query(models.Item).filter(models.Item.id == id).first()
    return item

@app.post('/item')
def add_item(request : schemas.Item, db : Session = Depends(get_db)):
    new_item = models.Item(name = request.name, price = request.price)
    db.add(new_item)
    db.commit()
    db.refresh(new_item)
    return new_item
