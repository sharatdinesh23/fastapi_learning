from fastapi import FastAPI
from api.v1.routes.user_route import user_router
from api.v1.routes.project_routes import project_router
from api.v1.routes.task_routes import task_router


app = FastAPI(
    title = "SaaS Project Management Platform",
    version  = "1.0.0"
)

app.include_router(user_router)
app.include_router(project_router)
app.include_router(task_router)
