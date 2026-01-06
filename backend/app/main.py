"""
FastAPI main application
"""
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from datetime import datetime

from .config.settings import settings
from .api import executive

# Create FastAPI app
app = FastAPI(
    title=settings.api_title,
    version=settings.api_version,
    description="REST API for SOC Executive Dashboard - Serves real-time security metrics from BigQuery",
    debug=settings.debug
)

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.cors_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(executive.router)

@app.get("/")
async def root():
    """Root endpoint"""
    return {
        "message": "SOC Executive Dashboard API",
        "version": settings.api_version,
        "status": "running",
        "timestamp": datetime.now().isoformat(),
        "docs": "/docs",
        "endpoints": {
            "executive_dashboard": "/api/executive/dashboard",
            "health": "/api/executive/health"
        }
    }

@app.get("/health")
async def health():
    """Health check endpoint"""
    return {
        "status": "healthy",
        "timestamp": datetime.now().isoformat()
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        "app.main:app",
        host=settings.api_host,
        port=settings.api_port,
        reload=settings.debug
    )
