from collections.abc import Callable
from functools import partial

from fastapi import FastAPI
from fastapi.responses import JSONResponse
from starlette import status
from starlette.requests import Request

from src.application.user.exceptions import (
    EmailAlreadyExist,
    InvalidJwtToken,
    InvalidPassword,
    UserIdNotExist,
    UsernameAlreadyExist,
    UsernameNotExist,
)
from src.domain.common.exceptions import AppException
from src.domain.user.entities.value_objects.email import WrongEmailValue
from src.domain.user.entities.value_objects.raw_password import WrongPasswordValue
from src.domain.user.entities.value_objects.username import WrongUsernameValue


def setup_exception_handlers(app: FastAPI) -> None:
    app.add_exception_handler(AppException, error_handler(500))
    app.add_exception_handler(UserIdNotExist, error_handler(status.HTTP_404_NOT_FOUND))
    app.add_exception_handler(
        UsernameNotExist, error_handler(status.HTTP_404_NOT_FOUND)
    )
    app.add_exception_handler(
        WrongUsernameValue, error_handler(status.HTTP_400_BAD_REQUEST)
    )
    app.add_exception_handler(
        UsernameAlreadyExist, error_handler(status.HTTP_409_CONFLICT)
    )
    app.add_exception_handler(
        EmailAlreadyExist, error_handler(status.HTTP_409_CONFLICT)
    )
    app.add_exception_handler(
        WrongEmailValue, error_handler(status.HTTP_400_BAD_REQUEST)
    )
    app.add_exception_handler(
        InvalidJwtToken, error_handler(status.HTTP_401_UNAUTHORIZED)
    )
    app.add_exception_handler(
        InvalidPassword, error_handler(status.HTTP_401_UNAUTHORIZED)
    )
    app.add_exception_handler(
        WrongPasswordValue, error_handler(status.HTTP_400_BAD_REQUEST)
    )
    app.add_exception_handler(Exception, unknown_exception_handler)


def error_handler(status_code: int) -> Callable[..., JSONResponse]:
    return partial(app_error_handler, status_code=status_code)


def app_error_handler(
    request: Request, err: AppException, status_code: int
) -> JSONResponse:
    return handle_error(
        request=request,
        err=err,
        err_data=err.title,
        status_code=status_code,
    )


def unknown_exception_handler(request: Request, err: Exception) -> JSONResponse:
    return JSONResponse(
        {"error": "Unknown error occurred"},
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
    )


def handle_error(
    request: Request,
    err: Exception,
    err_data: str,
    status_code: int,
) -> JSONResponse:
    print(err)
    return JSONResponse(
        {"detail": str(err_data)},
        status_code=status_code,
    )
