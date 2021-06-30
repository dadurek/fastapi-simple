from fastapi import HTTPException, status
from Utils import schemas, models
from sqlalchemy.orm import Session

def get_user_id(id : int, db : Session):
    user = db.query(models.User).filter(models.User.id == id).first()
    if not user: 
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Cannot find user with id = {id}")
    return user

def add_user(request : schemas.User, db : Session):
    user = models.User(login = request.login, password = request.password)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

def delete_user(id : int, db : Session):
    ammount = db.query(models.User).filter(models.User.id == id).delete(synchronize_session=False)
    if ammount != 1:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    db.commit()