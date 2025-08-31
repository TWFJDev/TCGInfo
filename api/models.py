from sqlalchemy import Column, Integer, String, DateTime, Text, ForeignKey
from sqlalchemy.orm import declarative_base, relationship
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
    card_text = Column(String)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

    extended_data = relationship("ExtendedData", back_populates="product", cascade="all, delete-orphan")

class ExtendedData(Base):
    __tablename__ = "extended_data"

    id = Column(Integer, primary_key=True)
    product_id = Column(Integer, ForeignKey("products.id"), nullable=False)
    name = Column(String(100))
    display_name = Column(String(255))
    value = Column(Text)  # long text fits your CardText description

    product = relationship("Product", back_populates="extended_data")

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
