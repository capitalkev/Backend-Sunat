from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.infrastructure.auth.firebase_init import initialize_firebase
from src.interfaces.router import sunat


def create_application() -> FastAPI:
    """
    Punto de entrada exclusivo para el Microservicio SUNAT.
    """
    application = FastAPI(
        title="API SUNAT - Capital Express",
        description="Microservicio dedicado a la integración y visualización de ventas SUNAT.",
        version="1.0.0",
    )
    initialize_firebase()

    origins = [
        "https://operaciones-capitalexpress.web.app",
    ]

    application.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    application.include_router(sunat.router)

    return application


app = create_application()
