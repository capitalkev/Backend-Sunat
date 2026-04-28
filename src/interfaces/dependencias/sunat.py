from typing import Annotated

from fastapi import Depends
from sqlalchemy.orm import Session

from src.application.sunat.get_empresas import GetEmpresas
from src.application.sunat.get_resumen import GetResumen  # <-- CAMBIADO
from src.application.sunat.get_ventas import GetVentas
from src.infrastructure.postgresql.connection_sunat import get_db
from src.infrastructure.postgresql.repositories_sunat.sunat import OperacionesRepository

DBSession = Annotated[Session, Depends(get_db)]


def dp_get_ventas(db: DBSession) -> GetVentas:
    return GetVentas(OperacionesRepository(db))


def dp_get_resumen(db: DBSession) -> GetResumen:
    return GetResumen(OperacionesRepository(db))


def dp_get_empresas(db: DBSession) -> GetEmpresas:
    return GetEmpresas(OperacionesRepository(db))
