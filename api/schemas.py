from pydantic import BaseModel, field_validator
from typing import Optional, Any, List
import json

class ProductBase(BaseModel):
    product_id: int
    name: str
    clean_name: Optional[str] = None
    image_url: Optional[str] = None
    url: Optional[str] = None
    modified_on: Optional[str] = None
    image_count: Optional[int] = None
    presale_info: Optional[Any] = None
    extended_data: Optional[Any] = None

    @field_validator("presale_info", "extended_data", mode="before")
    def parse_json_fields(cls, v):
        if isinstance(v, str):
            try:
                return json.loads(v)
            except Exception:
                return v
        return v

class ProductOut(ProductBase):
    class Config:
        orm_mode = True

class ProductListResponse(BaseModel):
    total_items: int
    limit: int
    results: List[ProductOut]

class PriceBase(BaseModel):
    product_id: int
    low_price: Optional[str] = None
    mid_price: Optional[str] = None
    high_price: Optional[str] = None
    market_price: Optional[str] = None
    direct_low_price: Optional[str] = None
    sub_type_name: Optional[str] = None


class PriceOut(PriceBase):
    class Config:
        orm_mode = True

class PriceListResponse(BaseModel):
    total_items: int
    limit: int
    results: List[PriceOut]