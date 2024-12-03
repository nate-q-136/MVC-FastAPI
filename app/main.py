# app/main.py
from fastapi import FastAPI
from app.db.session import engine, Base
from app.routers.api_routers import api_students_routers, api_classes_routers
from app.models import students, classes

# Tạo tất cả các bảng trong cơ sở dữ liệu
Base.metadata.create_all(bind=engine)

def get_application() -> FastAPI:
    application = FastAPI(
        title="FastAPI SQLite Project",
        docs_url="/docs",
        redoc_url="/re-docs",
        openapi_url="/api/v1/openapi.json",
    )
    return application

app = get_application()
app.include_router(api_students_routers, prefix="/api/v1", tags=["students-controller"])
app.include_router(api_classes_routers, prefix="/api/v1", tags=["classes-controller"])

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
