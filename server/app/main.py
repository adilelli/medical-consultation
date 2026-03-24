from fastapi import FastAPI
from app.api.user_router import router as user_router

app = FastAPI()

app.include_router(user_router)

@app.get("/")
def root():
    return {"message": "FastAPI Boilerplate Running"}