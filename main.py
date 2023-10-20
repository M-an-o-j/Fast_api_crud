from fastapi import FastAPI
from Items import Items_router

app = FastAPI(debug=True)

app.include_router(Items_router.router, prefix="/items", tags=["items"])