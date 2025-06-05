from typing import List, Optional

from pydantic import BaseModel, Field


class MatchResult(BaseModel):
    name: str
    table: int
    result: int

class Info(BaseModel):
    name: str
    version: str

class Player(BaseModel):
    name: str
    player_id: int

class Tournament(BaseModel):
    name: str
    code: Optional[str] = None
    tables: List[int]
    players: List[Player] = Field(default_factory=list)
    max_players: int = 30

