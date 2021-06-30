from fastapi import APIRouter, Depends, status
from Utils import schemas, database
from sqlalchemy.orm import Session
from Repository import user

router = APIRouter(
    prefix="/user",
    tags=["user"]
)

@router.get('/{id}', response_model = schemas.ShowUser, status_code = status.HTTP_200_OK)
def get_user_id(id : int, db : Session = Depends(database.get_db)):
    return user.get_user_id(id, db)

@router.post('/', status_code=status.HTTP_201_CREATED)
def add_user(request : schemas.User, db : Session = Depends(database.get_db)):
    return user.add_user(request,db)

@router.delete("/{id}", status_code=status.HTTP_200_OK)
def delete_user(id : int, db : Session = Depends(database.get_db)):
    return user.delete_user(id, db)