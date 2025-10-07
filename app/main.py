from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

API = FastAPI(title="Catalyst IQTrader API")

API.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@API.get("/health")
def health():
    return {"ok": True}


