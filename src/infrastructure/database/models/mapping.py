from . import Base, user_mapping


def start_mappers():
    mapper_registry = Base.registry
    user_mapping(mapper_registry)
