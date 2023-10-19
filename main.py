from fastapi import FastAPI
from routers import item

app = FastAPI(debug=True)

app.include_router(item.router, prefix="/items", tags=["items"])