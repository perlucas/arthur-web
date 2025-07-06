from sqlmodel import select

from src.sql.job_search import JobSearch
from src.common.database_gateway import DatabaseGateway

class JobSearchGateway(DatabaseGateway):

    def fetch_most_recent_job_searches(self, user_id: int) -> list[JobSearch]:
        statement = select(JobSearch).where(JobSearch.user_id == user_id)\
            .order_by(JobSearch.updated_at.desc())
        results = self._get_session().exec(statement)
        return results.all()