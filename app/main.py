from fastapi import FastAPI
from fastapi.openapi.utils import get_openapi
from app.api import auth, incidents
from app.db import database, models
from mangum import Mangum

# Initialize FastAPI app
app = FastAPI(title="Secure Incident Reporting System")

# Create database tables on startup
@app.on_event("startup")
def startup_event():
    models.Base.metadata.create_all(bind=database.engine)
    print("🚀 App has started. Database tables created.")

# Include routers
app.include_router(auth.router, prefix="/auth", tags=["auth"])
app.include_router(incidents.router, prefix="/incidents", tags=["incidents"])

# Root health-check
@app.get("/")
def root():
    return {"message": "Welcome to the Secure Incident Reporting API!"}

# Custom Swagger UI JWT authorization
def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema

    openapi_schema = get_openapi(
        title=app.title,
        version="1.0.0",
        description="API for reporting, tracking, and managing security incidents",
        routes=app.routes,
    )

    # JWT Bearer token support
    openapi_schema["components"]["securitySchemes"] = {
        "BearerAuth": {
            "type": "http",
            "scheme": "bearer",
            "bearerFormat": "JWT",
        }
    }

    for path in openapi_schema["paths"].values():
        for method in path.values():
            method["security"] = [{"BearerAuth": []}]

    app.openapi_schema = openapi_schema
    return app.openapi_schema

# Inject Swagger schema override
app.openapi = custom_openapi

# For AWS Lambda/Zappa compatibility
handler = Mangum(app)
