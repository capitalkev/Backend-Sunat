from typing import List, Protocol
from pyparsing import Optional


class SunatInterface(Protocol):

    def get_ventas_sire(
        self,
        ruc_empresa: Optional[List[str]],
        fecha_inicio: Optional[str],
        fecha_fin: Optional[str],
        monedas: Optional[List[str]],
        usuario_emails: Optional[List[str]],
    ):
        """Obtiene todas las facturas de la base de datos."""
        ...
