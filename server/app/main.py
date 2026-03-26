from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from app.api.consultation_router import router as consultation_router
from app.api.diagnosis_router import router as diagnosis_router
from app.api.user_router import router as user_router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

@app.exception_handler(ValueError)
async def value_error_exception_handler(request: Request, exc: ValueError):
    return JSONResponse(
        status_code=400,
        content={"detail": str(exc)}
    )

origins = [
    "http://localhost:3000",      # Nuxt dev server
    "http://localhost:8000",      # FastAPI itself (if needed)
    # Add your production frontend domain later
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,           # Allows specific origins
    allow_credentials=True,          # Allows cookies/auth headers
    allow_methods=["*"],             # Allows all HTTP methods
    allow_headers=["*"],             # Allows all headers
)

app.include_router(user_router)
app.include_router(consultation_router)
app.include_router(diagnosis_router)

@app.get("/")
def root():
    return {"message": "FastAPI Boilerplate Running"}