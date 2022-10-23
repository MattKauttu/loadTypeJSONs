from dataclasses import dataclass, field
from models.TypeRelationships import Relationships


@dataclass
class DualType:
    _type1name: str
    _defenses: Relationships
    _type2name: str = ""
