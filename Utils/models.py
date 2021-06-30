from sqlalchemy import Column, Integer, String, ForeignKey, Float
from Utils.database import Base
from sqlalchemy.orm import relationship

class Item(Base):
    __tablename__ =  'items'

    id = Column(Integer, primary_key = True, index=True)
    name = Column(String)
    price = Column(Float)
    user_id = Column(Integer, ForeignKey('users.id'))

    owner = relationship("User", back_populates="items")

class User(Base):
    __tablename__ =  'users'

    id = Column(Integer, primary_key = True, index=True)
    login = Column(String)
    password = Column(String)
    
    items = relationship('Item', back_populates="owner")