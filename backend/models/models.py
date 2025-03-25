from typing import List

from pydantic import BaseModel


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
    code: str
    tables: List[int]
    players: List[Player] = []

