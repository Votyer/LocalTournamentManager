import logging
from http.client import HTTPException
from typing import Dict

from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from fastapi.requests import Request
from starlette.responses import JSONResponse

from backend.models.models import Tournament, Player, MatchResult, Info

APP_NAME = "Tournament Manager"
VERSION = "0.1.0"

app = FastAPI()

# Abilita CORS per comunicare col frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

tournaments: Dict[str, Tournament] = {}


@app.exception_handler(Exception)
async def exception_handler(request: Request, exc: Exception):
    logging.exception("Unhandled error: %s", exc)
    return JSONResponse({"error": str(exc)}, status_code=500)
@app.get("/")
async def root():
    return Info(name=APP_NAME, version=VERSION)


@app.post("/createTournament")
async def create_tournament(tournament: Tournament):
    if tournament.code in tournaments:
        raise HTTPException("Tournament already exists")

    tournaments[tournament.name] = tournament
    return {"message": "Tournament created", "tournaments": list(tournaments.keys())}


@app.get("/tournaments")
async def get_tournaments():
    return list(tournaments.values())


@app.post("/joinTournament")
async def join_tournament(code: str, player: Player):
    tournament = find_tournament(code)

    if tournament is None:
        raise HTTPException("Tournament not found")

    if any(p.player_id == player.player_id for p in tournament.players):
        raise HTTPException("Tournament already joined")

    # Add player to tournament
    tournament.players.append(player)

    return tournament


@app.post("/submitResult")
async def submit_result(request: MatchResult):
    print(request)
    return {"result": "OK"}


def find_tournament(code: str):
    for tournament in tournaments.values():
        if tournament.code == code:
            return tournament
