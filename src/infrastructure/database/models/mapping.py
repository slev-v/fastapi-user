from . import Base, user_mapping


def start_mappers() -> None:
    mapper_registry = Base.registry
    user_mapping(mapper_registry)
