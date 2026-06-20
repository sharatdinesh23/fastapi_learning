from fastapi import APIRouter
from services.user_service import UserService

user_router = APIRouter(prefix="/users",tags= ["users"])

user_service = UserService()

@user_router.get("/read_users")
def get_users():
    return user_service.get_users()
