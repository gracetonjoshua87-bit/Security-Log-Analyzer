"""FastAPI application entry point."""
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from app.core.config import settings
from app.db.database import init_db
from app.api import auth, logs, threats, dashboard, reports, admin
from app.ml.classifier import get_model

app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION,
    description="AI-Powered Security Log Analyzer with Threat Detection",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.on_event("startup")
def on_startup():
    """Initialize DB, load ML model on startup."""
    init_db()
    get_model()  # trains + caches the classifier if it does not exist


@app.get("/", tags=["Root"])
def root():
    return {
        "app": settings.APP_NAME,
        "version": settings.APP_VERSION,
        "status": "operational",
        "docs": "/docs",
    }


@app.get("/api/v1/health", tags=["Health"])
def health():
    return {"status": "healthy"}


# Register routers under /api/v1
prefix = settings.API_V1_PREFIX
app.include_router(auth.router, prefix=prefix)
app.include_router(logs.router, prefix=prefix)
app.include_router(threats.router, prefix=prefix)
app.include_router(dashboard.router, prefix=prefix)
app.include_router(reports.router, prefix=prefix)
app.include_router(admin.router, prefix=prefix)
