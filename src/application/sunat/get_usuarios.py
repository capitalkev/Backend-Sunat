from src.domain.interfaces import SunatInterface
from src.domain.models import User


class GetUsuarios:
    def __init__(self, repository: SunatInterface) -> None:
        self.repository = repository

    def execute(self, current_user: User) -> list[dict[str, str]]:
        if not current_user.is_admin():
            return []
        return self.repository.get_usuarios_no_admin()
