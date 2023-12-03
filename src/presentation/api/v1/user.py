from fastapi import APIRouter, Depends

from src.application.user.use_cases import (GetUserById, GetUserByUsername,
                                            GetUsers, NewUser)
from src.application.user.use_cases.new_user import NewUserDTO
from src.di.stub import (get_user_by_id_stub, get_user_by_username_stub,
                         get_users_stub, new_user_stub)

router = APIRouter(prefix="/user", tags=["user"])


@router.get("/")
async def get_users(use_case: GetUsers = Depends(get_users_stub)):
    return list(await use_case())


@router.get("/{username}")
async def get_user_by_username(
    username: str,
    use_case: GetUserByUsername = Depends(get_user_by_username_stub),
):
    return await use_case(username)


@router.get("/by_id/{user_id}")
async def get_user_by_id(
    id: int,
    use_case: GetUserById = Depends(get_user_by_id_stub),
):
    return await use_case(id)


@router.post("/")
async def new_user(data: NewUserDTO, use_case: NewUser = Depends(new_user_stub)):
    return await use_case(data)
