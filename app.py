from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from api.routes.products import router as products_router
from api.routes.prices import router as prices_router
from api.db import engine
from api.models import Base

# Create DB tables if they don't exist
Base.metadata.create_all(bind=engine)

app = FastAPI(title="TCGCSV Scraper API", version="0.1.0")

# CORS (adjust in production)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(products_router)
app.include_router(prices_router)

@app.get("/")
def root():
    return {"message": "TCGCSV Scraper API - see /docs for interactive API"}
