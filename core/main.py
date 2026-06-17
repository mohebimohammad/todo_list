from fastapi import FastAPI
from contextlib import asynccontextmanager
from tasks.routes import router as tasks_routes
from tags_metadata import tags_metadata

@asynccontextmanager
async def lifespan(app: FastAPI):
    print("Application startup")
    yield
    print("Application shutdown")

app = FastAPI(
        title="Todo Application",
        description="description",
        version="0.0.1",
        terms_of_servie="http://example.com/terms/",
        contact={
            "name": "Mohammad Mohebi",
            "url":"https://mysite.ir",
            "email":"muhammadmohebi123@gmail.com"},
        license_info={
            "name": "MIT"
            }, lifespan=lifespan, openapi_tags=tags_metadata
        )

app.include_router(tasks_routes,prefix="/api/v1")

