# src/inventory.py
from sqlalchemy import create_engine, Column, Integer, String, Sequence
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///inventory.db')
Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()

class InventoryItem(Base):
    __tablename__ = 'inventory'
    id = Column(Integer, Sequence('item_id_seq'), primary_key=True)
    name = Column(String(50))
    category = Column(String(50))
    stock = Column(Integer)
    reorder = Column(Integer)

def add_inventory_item(name, category, stock, reorder):
    """Add an item to the inventory."""
    item = InventoryItem(name=name, category=category, stock=stock, reorder=reorder)
    session.add(item)
    session.commit()
    return item

def get_all_inventory_items():
    """Retrieve all inventory items."""
    return session.query(InventoryItem).all()

def setup_database():
    """Setup the database."""
    Base.metadata.create_all(engine)
