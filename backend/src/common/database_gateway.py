from fastapi import Depends
from sqlmodel import create_engine, Session
from sqlalchemy import Engine
from os import getenv
from typing import Annotated

_engine: Engine | None = None

def get_engine() -> Engine:
    global _engine
    if _engine is None:
        _engine = create_engine(getenv("DB_URL"))
    return _engine


EngineDep = Annotated[Engine, Depends(get_engine)]

def get_session(engine: EngineDep):
    with Session(engine) as session:
        yield session

SessionDep = Annotated[Session, Depends(get_session)]


class DatabaseGateway:
    _session: Session
    _engine: Engine

    def __init__(self, session: SessionDep, engine: EngineDep):
        self._session = session
        self._engine = engine

    def _get_engine(self) -> Engine:
        return self._engine

    def _get_session(self) -> Session:
        return self._session
    


__all__ = ['DatabaseGateway', 'SessionDep', 'EngineDep']
    