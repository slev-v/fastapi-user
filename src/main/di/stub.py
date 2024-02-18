# db and repos


def get_redis_stub() -> None:
    raise NotImplementedError


def get_session_stub() -> None:
    raise NotImplementedError


def provide_user_repo_stub() -> None:
    raise NotImplementedError


def provide_redis_repo_stub() -> None:
    raise NotImplementedError


# services


def provide_hasher_password_stub() -> None:
    raise NotImplementedError


def provide_session_service_stub() -> None:
    raise NotImplementedError


# use_cases


def provide_login_stub() -> None:
    raise NotImplementedError


def provide_logout_stub() -> None:
    raise NotImplementedError


def provide_get_users_stub() -> None:
    raise NotImplementedError


def provide_new_user_stub() -> None:
    raise NotImplementedError


def provide_delete_user_stub() -> None:
    raise NotImplementedError


def provide_get_user_by_session_id_stub() -> None:
    raise NotImplementedError


def provide_get_user_by_id_stub() -> None:
    raise NotImplementedError


def provide_get_user_by_username_stub() -> None:
    raise NotImplementedError
