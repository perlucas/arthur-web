from src.common.use_case import UseCase, UseCaseResult
from src.common.json_presenter import JsonPresenter
from src.sql.job_search import JobSearch
from src.job_search.services.job_search_gateway import JobSearchGateway
from src.auth.services.auth_service import AuthService
from src.job_search.use_cases.common import JobSearchOutput

class ListJobSearchesUseCase(UseCase):

    def __init__(self, gateway: JobSearchGateway, auth: AuthService):
        self._gateway = gateway
        self._auth = auth

    def execute(self) -> UseCaseResult[list[JobSearch]]:
        # 1. Fetch & retrieve the job searches for the current user
        job_searches = self._gateway.fetch_most_recent_job_searches(
            user_id=self._auth.current_user().id,
        )

        return UseCaseResult[list[JobSearch]](result=job_searches)



response_model = list[JobSearchOutput]


class ListJobSearchesPresenter(JsonPresenter):
    
    def _present_success(self, result: UseCaseResult[list[JobSearch]]) -> response_model:
        return [x for x in result.result()]