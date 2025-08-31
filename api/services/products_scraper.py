import requests
from sqlalchemy.orm import Session
from typing import Optional
import json
import time

# Import local DB models and engine
from ..models import Product, ExtendedData, Base
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

    # Check if product already exists
    existing = session.query(Product).filter(Product.product_id == product_id).first()
    if existing:
        return  # Skip duplicates, or you could update fields here

    # Create Product and loop through extendedData
    product = Product(
        product_id=product_id,
        name=name,
        clean_name=clean_name,
        image_url=image_url,
        url=url,
        modified_on=modified_on,
        image_count=image_count,
        extended_data=[
            ExtendedData(
                name=ext.get("name"),
                display_name=ext.get("displayName"),
                value=ext.get("value"),
            )
            for ext in item.get("extendedData", [])
        ]
    )

    # Optional: extract CardText for quick access
    card_text_item = next((ext for ext in item.get("extendedData", []) if ext.get("name") == "CardText"), None)
    if card_text_item:
        product.card_text = card_text_item.get("value")

    session.add(product)
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
