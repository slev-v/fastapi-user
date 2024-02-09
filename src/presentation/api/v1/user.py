from fastapi import APIRouter, Cookie, Depends, Response, status

from src.application.user.dto import (
    SessionResponseDTO,
    UserLoginRequestDTO,
    UserRequestDTO,
    UserResponseDTO,
    UsersResponseDTO,
)
from src.application.user.use_cases import (
    DeleteUser,
    GetUserById,
    GetUserByUsername,
    GetUsers,
    NewUser,
    UserLogin,
    UserLogout,
)
from src.main.di.stub import (
    provide_delete_user_stub,
    provide_get_user_by_id_stub,
    provide_get_user_by_session_id_stub,
    provide_get_user_by_username_stub,
    provide_get_users_stub,
    provide_login_stub,
    provide_logout_stub,
    provide_new_user_stub,
)

router = APIRouter(prefix="/user", tags=["user"])


@router.post("/", status_code=status.HTTP_201_CREATED)
async def new_user(
    data: UserRequestDTO,
    use_case: NewUser = Depends(provide_new_user_stub),
) -> dict[str, str]:
    user_id = await use_case(data)
    return {"message": f"User with id {user_id} created successfully"}


@router.get("/")
async def get_users(
    use_case: GetUsers = Depends(provide_get_users_stub),
) -> UsersResponseDTO:
    return await use_case()


@router.delete("/")
async def delete_user(
    session_id: str = Cookie(include_in_schema=False),
    use_case: DeleteUser = Depends(provide_delete_user_stub),
) -> dict[str, str]:
    await use_case(session_id)
    return {"message": "User deleted successfully"}


@router.post("/login")
async def login(
    response: Response,
    data: UserLoginRequestDTO,
    use_case: UserLogin = Depends(provide_login_stub),
) -> SessionResponseDTO:
    session_id = await use_case(data)
    response.set_cookie("session_id", session_id, httponly=True)
    return SessionResponseDTO(session_id=session_id)


@router.post("/logout", status_code=status.HTTP_204_NO_CONTENT)
async def logout(
    response: Response,
    session_id: str = Cookie(include_in_schema=False),
    use_case: UserLogout = Depends(provide_logout_stub),
) -> None:
    await use_case(session_id)
    response.delete_cookie("session_id")


@router.get("/me")
async def get_current_user(
    session_id: str = Cookie(include_in_schema=False),
    use_case: GetUserByUsername = Depends(provide_get_user_by_session_id_stub),
) -> UserResponseDTO:
    user = await use_case(session_id)
    return user


@router.get("/by_id/{user_id}")
async def get_user_by_id(
    user_id: int,
    use_case: GetUserById = Depends(provide_get_user_by_id_stub),
) -> UserResponseDTO:
    user = await use_case(user_id)
    return user


@router.get("/{username}")
async def get_user_by_username(
    username: str,
    use_case: GetUserByUsername = Depends(provide_get_user_by_username_stub),
) -> UserResponseDTO:
    user = await use_case(username)
    return user
