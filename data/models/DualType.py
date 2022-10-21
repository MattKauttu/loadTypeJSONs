from dataclasses import dataclass
from models.TypeRelationships import Relationships


@dataclass
class DualType:
    _type1name: str
    type2name: str
    defenses: Relationships
