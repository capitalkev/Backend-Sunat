from typing import List, Protocol, Optional, Dict, Any


class SunatInterface(Protocol):
    def get_ventas_sire(
        self,
        ruc_empresa: Optional[List[str]],
        fecha_inicio: Optional[str],
        fecha_fin: Optional[str],
        monedas: Optional[List[str]],
        usuario_emails: Optional[List[str]],
        page: int,
        page_size: int,
        sort_by: str,
    ) -> Dict[str, Any]: ...

    def get_metricas_resumen(
        self,
        ruc_empresa: Optional[List[str]],
        fecha_inicio: Optional[str],
        fecha_fin: Optional[str],
        monedas: Optional[List[str]],
        usuario_emails: Optional[List[str]],
    ) -> Dict[str, Any]:
        """Obtiene las métricas KPIs agrupadas por moneda (PEN, USD)"""
        ...

    def update_venta_estado(self, venta_id: str, estado: str) -> bool:
        """Actualiza el estado1 de una factura"""
        ...

    def get_empresas(self, usuario_emails: Optional[List[str]]) -> List[Dict[str, str]]:
        """Obtiene la lista de clientes/empresas únicos"""
        ...

    def get_usuarios_no_admin(self) -> List[Dict[str, str]]:
        """Obtiene la lista de usuarios para los filtros"""
        ...
