from sqlmodel import func, select

from src.sql.job_search import JobSearch
from src.common.database_gateway import DatabaseGateway

class JobSearchGateway(DatabaseGateway):

    def fetch_most_recent_job_searches(self, user_id: int) -> list[JobSearch]:
        statement = select(JobSearch).where(JobSearch.user_id == user_id)\
            .order_by(JobSearch.updated_at.desc())
        results = self._get_session().exec(statement)
        return results.all()
    
    def count_user_job_searches(self, user_id: int, count_all = False, active_only = True, inactive_only = False) -> int:
        statement = select(func.count(JobSearch.id)).where(JobSearch.user_id == user_id)
        if not count_all:
            if active_only:
                statement = statement.where(JobSearch.is_active)
            elif inactive_only:
                statement = statement.where(JobSearch.is_active == False)
        
        results = self._get_session().exec(statement)
        return results.one()


    def save_job_search(self, search: JobSearch) -> JobSearch:
        session = self._get_session()
        session.add(search)
        session.commit()
        session.refresh(search)
        return search
