from fastapi.params import Depends
from requests import Session

from src.application.sunat import SunatUseCases
from src.infrastructure.postgresql.connection_sunat import get_db
from src.infrastructure.postgresql.repositories_sunat.sunat import OperacionesRepository


def get_sunat_use_cases(db: Session = Depends(get_db)) -> SunatUseCases:
    repo = OperacionesRepository(db)
    return SunatUseCases(repo)
