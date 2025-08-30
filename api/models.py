from sqlalchemy import Column, Integer, String, DateTime, Text, JSON
from sqlalchemy.orm import declarative_base
from sqlalchemy.sql import func

Base = declarative_base()

class Product(Base):
    __tablename__ = "products"
    id = Column(Integer, primary_key=True, index=True)
    product_id = Column(Integer, index=True, nullable=False, unique=True)
    name = Column(String, nullable=False)
    clean_name = Column(String)
    image_url = Column(String)
    url = Column(String)
    modified_on = Column(String)
    image_count = Column(Integer)
    presale_info = Column(JSON)
    extended_data = Column(JSON)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

class Price(Base):
    __tablename__ = "prices"
    id = Column(Integer, primary_key=True, index=True)
    product_id = Column(Integer, index=True, nullable=False)
    low_price = Column(String, nullable=False)
    mid_price = Column(String)
    high_price = Column(String)
    market_price = Column(String)
    direct_low_price = Column(String)
    sub_type_name = Column(String)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
