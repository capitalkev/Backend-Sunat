from fastapi import APIRouter, Depends, Query, Path, Body, HTTPException
from typing import List, Optional

from src.application.sunat import SunatUseCases
from src.interfaces.dependencias.auth import get_current_user
from src.interfaces.dependencias.sunat import get_sunat_use_cases

router = APIRouter(prefix="/api", tags=["Sunat"])


@router.get("/ventas")
def get_ventas(
    fecha_desde: Optional[str] = Query(None),
    fecha_hasta: Optional[str] = Query(None),
    moneda: Optional[List[str]] = Query(None),
    rucs_empresa: Optional[List[str]] = Query(None),
    usuario_emails: Optional[List[str]] = Query(None),
    page: int = Query(1, ge=1),
    page_size: int = Query(20, ge=1),
    sort_by: str = Query("fecha"),
    use_cases: SunatUseCases = Depends(get_sunat_use_cases),
    current_user=Depends(get_current_user),
):
    filters = {
        "fecha_desde": fecha_desde,
        "fecha_hasta": fecha_hasta,
        "monedas": moneda,
        "rucs_empresa": rucs_empresa,
        "usuario_emails": usuario_emails,
        "page": page,
        "page_size": page_size,
        "sort_by": sort_by,
    }
    return use_cases.get_ventas(user_session=current_user, filters=filters)


@router.get("/metricas/resumen")
def get_metricas(
    fecha_desde: Optional[str] = Query(None),
    fecha_hasta: Optional[str] = Query(None),
    moneda: Optional[List[str]] = Query(None),
    rucs_empresa: Optional[List[str]] = Query(None),
    usuario_emails: Optional[List[str]] = Query(None),
    use_cases: SunatUseCases = Depends(get_sunat_use_cases),
    current_user=Depends(get_current_user),
):
    filters = {
        "fecha_desde": fecha_desde,
        "fecha_hasta": fecha_hasta,
        "monedas": moneda,
        "rucs_empresa": rucs_empresa,
        "usuario_emails": usuario_emails,
    }
    return use_cases.get_metricas(user_session=current_user, filters=filters)


@router.put("/ventas/{venta_id}/estado")
def update_venta_estado(
    venta_id: str = Path(...),
    payload: dict = Body(...),
    use_cases: SunatUseCases = Depends(get_sunat_use_cases),
    current_user=Depends(get_current_user),
):
    nuevo_estado = payload.get("estado1")
    if not nuevo_estado:
        raise HTTPException(status_code=400, detail="El campo 'estado1' es requerido")

    actualizado = use_cases.update_estado(venta_id, nuevo_estado)
    if not actualizado:
        raise HTTPException(status_code=404, detail="Factura no encontrada")

    return {"message": "Estado actualizado correctamente"}


@router.get("/ventas/empresas")
def get_empresas(
    usuario_emails: Optional[List[str]] = Query(None),
    use_cases: SunatUseCases = Depends(get_sunat_use_cases),
    current_user=Depends(get_current_user),
):
    return use_cases.get_empresas(
        user_session=current_user, usuario_emails=usuario_emails
    )


@router.get("/usuarios/no-admin")
def get_usuarios(
    use_cases: SunatUseCases = Depends(get_sunat_use_cases),
    current_user=Depends(get_current_user),
):
    return use_cases.get_usuarios()
