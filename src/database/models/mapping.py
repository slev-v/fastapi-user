from src.database.models import user_mapping
from src.database.models.base import Base


def start_mappers():
    mapper_registry = Base.registry
    user_mapping(mapper_registry)
