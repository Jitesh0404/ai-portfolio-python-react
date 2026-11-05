from fastapi import APIRouter
from ai_portfolio.controllers import user_controller

router = APIRouter(prefix="/users", tags=["users"])


@router.get("/user")
def get_users():
    return user_controller.get_all_users()
