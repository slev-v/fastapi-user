from dataclasses import dataclass, field


@dataclass
class Entity:
    id: int = field(init=False)
