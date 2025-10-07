from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .market import router as market_router   # <— add this line

API = FastAPI(title="Catalyst IQTrader API")
API.add_middleware(CORSMiddleware, allow_origins=["*",], allow_methods=["*"], allow_headers=["*"])

@API.get("/health")
def health():
    return {"ok": True}

API.include_router(market_router)            # <— and this line


