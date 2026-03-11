from sqlalchemy import text
from sqlalchemy.orm import Session
from typing import List, Optional

from src.domain.interfaces import SunatInterface


class OperacionesRepository(SunatInterface):
    def __init__(self, db: Session):
        self.db = db

    def get_ventas_sire(
        self,
        ruc_empresa: Optional[List[str]],
        fecha_inicio: Optional[str],
        fecha_fin: Optional[str],
        monedas: Optional[List[str]],
        usuario_emails: Optional[List[str]],
    ):
        query_str = """
            SELECT 
                f.ruc, f.razon_social, f.moneda, 
                f.serie_cdp, f.nro_cp_inicial, f.periodo,
                f.total_cp AS total_factura,
                COALESCE(nc.total_cp, 0) AS total_nota_credito,
                (f.total_cp + COALESCE(nc.total_cp, 0)) AS saldo_neto
            FROM ventas_sire f
            JOIN enrolados en ON f.ruc = en.ruc
            LEFT JOIN ventas_sire nc 
                ON f.ruc = nc.ruc 
                AND f.nro_cp_inicial = CAST(CAST(CAST(nc.nro_cp_modificado AS FLOAT) AS INT) AS VARCHAR)
                AND f.serie_cdp = nc.serie_cp_modificado 
                AND nc.tipo_cp_doc = '7'
            WHERE f.tipo_cp_doc = '1'
        """

        params = {}

        # Filtro de Seguridad / Ejecutivo
        # Si usuario_emails tiene datos, restringimos la vista
        if usuario_emails:
            query_str += " AND en.email IN :emails"
            params["emails"] = tuple(usuario_emails)

        # Filtros opcionales del Frontend (hooks.ts)
        if ruc_empresa:
            query_str += " AND f.ruc IN :rucs"
            params["rucs"] = tuple(ruc_empresa)

        if fecha_inicio and fecha_fin:
            query_str += " AND f.fecha_emision BETWEEN :inicio AND :fin"
            params["inicio"] = fecha_inicio
            params["fin"] = fecha_fin

        if monedas:
            query_str += " AND f.moneda IN :monedas"
            params["monedas"] = tuple(monedas)

        result = self.db.execute(text(query_str), params)
        return [dict(row) for row in result.mappings()]
