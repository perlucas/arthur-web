from src.sql.user import User
from src.common.database_gateway import DatabaseGateway

class UserGateway(DatabaseGateway):

    def fetch_testing_user(self) -> User | None:
        return self._get_session().get(User, 1)