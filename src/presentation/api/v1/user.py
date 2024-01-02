from fastapi import APIRouter, Depends, HTTPException, Response, status

from src.application.user.dto import (
    TokenResponseDTO,
    UserLoginRequestDTO,
    UserRequestDTO,
    UserResponseDTO,
    UsersResponseDTO,
)
from src.application.user.exceptions.user import AuthError
from src.application.user.use_cases import (
    DeleteUser,
    GetUserById,
    GetUserByUsername,
    GetUsers,
    NewUser,
    UserLogin,
)
from src.main.di.stub import (
    delete_user_stub,
    get_user_by_id_stub,
    get_user_by_username_stub,
    get_username_from_cookie_stub,
    get_users_stub,
    new_user_stub,
    user_login_stub,
)

router = APIRouter(prefix="/user", tags=["user"])


@router.post("/", status_code=status.HTTP_201_CREATED)
async def new_user(
    data: UserRequestDTO,
    use_case: NewUser = Depends(new_user_stub),
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


@router.delete("/")
async def delete_user(
    username: str = Depends(get_username_from_cookie_stub),
    use_case: DeleteUser = Depends(delete_user_stub),
) -> dict[str, str]:
    await use_case(username)
    return {"message": "User deleted successfully"}


@router.post("/login")
async def login(
    response: Response,
    data: UserLoginRequestDTO,
    use_case: UserLogin = Depends(user_login_stub),
) -> TokenResponseDTO:
    try:
        token = await use_case(data)
    except AuthError as e:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=str(e))
    response.set_cookie("access_token", token, httponly=True)
    return TokenResponseDTO(access_token=token, token_type="bearer")


@router.get("/me")
async def get_user_from_cookie(
    username: str = Depends(get_username_from_cookie_stub),
    use_case: GetUserByUsername = Depends(get_user_by_username_stub),
) -> UserResponseDTO:
    user = await use_case(username)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="User not found"
        )
    return user


@router.get("/by_id/{user_id}")
async def get_user_by_id(
    user_id: int,
    use_case: GetUserById = Depends(get_user_by_id_stub),
) -> UserResponseDTO:
    user = await use_case(user_id)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="User not found"
        )
    return user


@router.get("/{username}")
async def get_user_by_username(
    username: str,
    use_case: GetUserByUsername = Depends(get_user_by_username_stub),
) -> UserResponseDTO:
    user = await use_case(username)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="User not found"
        )
    return user
