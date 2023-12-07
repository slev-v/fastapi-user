from fastapi import APIRouter, Depends, HTTPException, status

from src.application.user.dto.user_dto import (UserRequestDTO, UserResponseDTO,
                                               UsersResponseDTO)
from src.application.user.exceptions.user import AuthError
from src.application.user.services.hasher_password import HasherPassword
from src.application.user.use_cases import (GetUserById, GetUserByUsername,
                                            GetUsers, NewUser)
from src.di.stub import (get_user_by_id_stub, get_user_by_username_stub,
                         get_users_stub, new_user_stub)

router = APIRouter(prefix="/user", tags=["user"])


@router.post("/")
async def new_user(
    data: UserRequestDTO, use_case: NewUser = Depends(new_user_stub)
) -> dict[str, str]:
    try:
        await use_case(data)
    except AuthError as e:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail=str(e)
        )
    return {"message": "User created successfully"}


@router.get("/")
async def get_users(use_case: GetUsers = Depends(get_users_stub)) -> UsersResponseDTO:
    return await use_case()


@router.get("/testtest")
async def test():
    return HasherPassword().get_password_hash("testtest")


@router.get("/by_id/{user_id}")
async def get_user_by_id(
    id: int,
    use_case: GetUserById = Depends(get_user_by_id_stub),
):
    user = await use_case(id)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="User not found"
        )
    return user


@router.get("/{username}")
async def get_user_by_username(
    username: str,
    use_case: GetUserByUsername = Depends(get_user_by_username_stub),
):
    user = await use_case(username)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="User not found"
        )
    return user
