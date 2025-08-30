from fastapi import APIRouter, Depends, HTTPException, BackgroundTasks, Query
from sqlalchemy.orm import Session
from typing import List, Optional

from ..db import get_db
from ..models import Product, Base
from ..schemas import ProductOut, ProductListResponse
from ..services.products_scraper import scrape_group, scrape_all

router = APIRouter(prefix="/products", tags=["products"])

@router.get("", response_model=ProductListResponse)
def list_products(skip: int = 0, limit: int = 50, search: Optional[str] = Query(None), db: Session = Depends(get_db)):
    q = db.query(Product)
    total_items = q.count()
    if search:
        q = q.filter(Product.name.ilike(f"%{search}%"))
    items = q.offset(skip).limit(limit).all()

    query = {}
    query["total_items"] = total_items
    query["limit"] = limit
    query["results"] = items
    return query

@router.get("/{product_id}", response_model=ProductOut)
def get_product(product_id: int, db: Session = Depends(get_db)):
    item = db.query(Product).filter(Product.product_id == product_id).first()
    if not item:
        raise HTTPException(status_code=404, detail="Product not found")
    return item

@router.post("/scrape/group/{group_id}")
def trigger_scrape_group(group_id: int, background_tasks: BackgroundTasks):
    # schedule scraping in background (non-blocking)
    background_tasks.add_task(scrape_group, group_id)
    return {"status": "scheduled", "group_id": group_id}

@router.post("/scrape/all")
def trigger_scrape_all(background_tasks: BackgroundTasks):
    background_tasks.add_task(scrape_all)
    return {"status": "scheduled_all"}
