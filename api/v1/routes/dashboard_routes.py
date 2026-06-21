from fastapi import APIRouter
from services.dashboard_service import DashboardService

dashboard_router = APIRouter()

dashboard_service = DashboardService()

@dashboard_router.get("/dashboard")
async def get_dashboard():
    return await dashboard_service.get_dashboard_data()
