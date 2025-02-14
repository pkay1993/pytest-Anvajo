from dataclasses import dataclass
from typing import List, Optional


@dataclass(frozen=False) # Frozen macht die Instanz unveränderbar. Damit kann ich test das alter nicht geändert werden
class Person:
    name: str
    age: int
    hobbies: List[str]
    nickname: Optional[str] = None
