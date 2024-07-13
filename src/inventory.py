from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()
engine = create_engine('sqlite:///inventory.db')
Session = sessionmaker(bind=engine)
session = Session()

class Inventory(Base):
    __tablename__ = 'inventory'
    id = Column(Integer, primary_key=True)
    product_name = Column(String)
    category = Column(String)
    stock_level = Column(Integer)
    reorder_level = Column(Integer)

Base.metadata.create_all(engine)

def add_product(name, category, stock, reorder):
    new_product = Inventory(product_name=name, category=category, stock_level=stock, reorder_level=reorder)
    session.add(new_product)
    session.commit()

def get_inventory():
    return session.query(Inventory).all()

