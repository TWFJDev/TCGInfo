import requests
from sqlalchemy.orm import Session
from typing import Optional
import json
import time

# Import local DB models and engine
from ..models import Product, Base
from ..db import engine, SessionLocal

# Ensure tables exist
Base.metadata.create_all(bind=engine)

TCGCSV_BASE = "https://tcgcsv.com/tcgplayer/3"

def _save_product_to_db(session: Session, item: dict):
    product_id = int(item.get("productId") or item.get("id") or 0)
    name = item.get("name") or item.get("productName") or "Unknown"
    clean_name = item.get("cleanName")
    image_url = item.get("imageUrl")
    url = item.get("url")
    modified_on = item.get("modifiedOn")
    image_count = item.get("imageCount")
    presale_info = json.dumps(item.get("presaleInfo", []))
    extended_data = json.dumps(item.get("extendedData", []))

    existing = session.query(Product).filter(Product.product_id == product_id).first()
    if existing:
        existing.name = name
        existing.clean_name = clean_name
        existing.image_url = image_url
        existing.url = url
        existing.modified_on = modified_on
        existing.image_count = image_count
        existing.presale_info = presale_info
        existing.extended_data = extended_data
    else:
        p = Product(
            product_id=product_id,
            name=name,
            clean_name=clean_name,
            image_url=image_url,
            url=url,
            modified_on=modified_on,
            image_count=image_count,
            presale_info=presale_info,
            extended_data=extended_data
        )
        session.add(p)
    session.commit()

def scrape_group(group_id: int):
    session = SessionLocal()
    try:
        url = f"{TCGCSV_BASE}/{group_id}/products"
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
