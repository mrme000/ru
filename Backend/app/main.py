import sys
import os

from fastapi import FastAPI
from app.api.routes import router
from app.core.config import settings
from mangum import Mangum

# Create FastAPI app with metadata
app = FastAPI(
    title=settings.app_name,
    description="Backend API for RU Carpooling service - Rutgers University students carpooling platform",
    version="1.0.0",
    debug=settings.debug
)

# Include the router
app.include_router(router)

@app.get("/")
def read_root():
    return {"message": "Welcome to the RU Carpooling API!", "version": "1.0.0"}

@app.get("/health")
def health_check():
    return {"status": "healthy", "app": settings.app_name}

# Define the handler for AWS Lambda
handler = Mangum(app)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)
