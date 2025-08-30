import requests
from sqlalchemy.orm import Session
from typing import Optional
import time

# Import local DB models and engine
from ..models import Price, Base
from ..db import engine, SessionLocal

# Ensure tables exist
Base.metadata.create_all(bind=engine)

TCGCSV_BASE = "https://tcgcsv.com/tcgplayer/3"

def _save_product_to_db(session: Session, item: dict):
    product_id = int(item.get("productId") or item.get("id") or 0)
    low_price = item.get("lowPrice")
    mid_price = item.get("midPrice")
    high_price = item.get("highPrice")
    market_price = item.get("marketPrice")
    direct_low_price = item.get("directLowPrice")
    sub_type_name = item.get("subTypeName")

    existing = session.query(Price).filter(Price.product_id == product_id).filter(Price.sub_type_name == sub_type_name).first()
    if existing:
        existing.low_price = low_price
        existing.mid_price = mid_price
        existing.high_price = high_price
        existing.market_price = market_price
        existing.direct_low_price = direct_low_price
        existing.sub_type_name = sub_type_name
    else:
        p = Price(
            product_id=product_id,
            low_price=low_price,
            mid_price=mid_price,
            high_price=high_price,
            market_price=market_price,
            direct_low_price=direct_low_price,
            sub_type_name=sub_type_name
        )
        session.add(p)
    session.commit()

def scrape_group(group_id: int):
    session = SessionLocal()
    try:
        url = f"{TCGCSV_BASE}/{group_id}/prices"
        r = requests.get(url, timeout=30)
        r.raise_for_status()
        data = r.json().get("results", [])
        for i, item in enumerate(data, 1):
            _save_product_to_db(session, item)
        return {"status": "ok", "count": len(data)}
    finally:
        session.close()

def scrape_all():
    session = SessionLocal()
    try:
        url = f"{TCGCSV_BASE}/groups"
        r = requests.get(url, timeout=30)
        r.raise_for_status()
        groups = r.json().get("results", [])
        for g in groups:
            gid = g.get("groupId") or g.get("id")
            try:
                scrape_group(gid)
                time.sleep(0.2)
            except Exception as e:
                print(f"Failed group {gid}: {e}")
        return {"status": "done", "groups": len(groups)}
    finally:
        session.close()
