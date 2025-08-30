from fastapi import APIRouter, Depends, HTTPException, BackgroundTasks, Query
from sqlalchemy.orm import Session
from typing import List, Optional

from ..db import get_db
from ..models import Price, Base
from ..schemas import PriceOut, PriceListResponse
from ..services.prices_scraper import scrape_group, scrape_all

router = APIRouter(prefix="/prices", tags=["prices"])

@router.get("", response_model=PriceListResponse)
def list_prices(skip: int = 0, limit: int = 50, product_id: Optional[int] = Query(None), db: Session = Depends(get_db)):
    q = db.query(Price)
    total_items = q.count()
    if product_id is not None:
        q = q.filter(Price.product_id == product_id)
    items = q.offset(skip).limit(limit).all()

    query = {}
    query["total_items"] = total_items
    query["limit"] = limit
    query["results"] = items
    return query

@router.get("/{product_id}", response_model=PriceOut)
def get_price(product_id: int, db: Session = Depends(get_db)):
    item = db.query(Price).filter(Price.product_id == product_id).first()
    if not item:
        raise HTTPException(status_code=404, detail="Price not found")
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