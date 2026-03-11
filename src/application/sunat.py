from src.infrastructure.postgresql.repositories_sunat.sunat import OperacionesRepository


class GetVentasUseCase:
    def __init__(self, repo: OperacionesRepository):
        self.repo = repo

    def execute(self, user_session, filters: dict):
        """
        user_session: contiene el rol y email del usuario logueado
        filters: filtros enviados desde el componente Filters.tsx
        """
        usuario_emails = filters.get("usuario_emails")

        if not user_session.permissions.is_admin:
            usuario_emails = [user_session.email]
        else:
            pass

        return self.repo.get_ventas_sire(
            ruc_empresa=filters.get("rucs_empresa"),
            fecha_inicio=filters.get("fecha_desde"),
            fecha_fin=filters.get("fecha_hasta"),
            monedas=filters.get("monedas"),
            usuario_emails=usuario_emails,
        )
