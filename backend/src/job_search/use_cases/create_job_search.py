from typing import Annotated
from datetime import datetime

from pydantic import BaseModel, Field, AfterValidator
from fastapi.encoders import jsonable_encoder

from src.common.use_case import UseCase, UseCaseResult
from src.common.json_presenter import JsonPresenter
from src.sql.job_search import JobSearch
from src.job_search.services.job_search_gateway import JobSearchGateway
from src.auth.services.auth_service import AuthService
from src.job_search.use_cases.common import (
    JobSearchOutput,
    JobSearchParameters,
    is_valid_location,
    PlanExpired,
    UserLimitsError,
    PlanLimitsError,
)
from src.plan import plans

class NewJobSearch(BaseModel):
    name: str = Field(min_length=3)
    is_active: bool
    location: Annotated[str, AfterValidator(is_valid_location)]
    search_parameters: JobSearchParameters
    setting_send_email_notifications: bool


class CreateJobSearchUseCase(UseCase):
    MAX_JOB_SEARCHES_ALLOWED = 25

    def __init__(self, gateway: JobSearchGateway, auth: AuthService):
        self._gateway = gateway
        self._auth = auth

    def execute(self, input: NewJobSearch) -> UseCaseResult[JobSearch]:
        # 1. Validate that user's current plan has not expired
        current_expiration_date = self._auth.current_user().plan_expires_on
        if current_expiration_date < datetime.now():
            return UseCaseResult[None](None, PlanExpired())

        # 2. Validate that user has not reached max limit
        count_all_searches = self._gateway.count_user_job_searches(
            user_id=self._auth.current_user().id,
            count_all=True
        )
        if count_all_searches >= self.MAX_JOB_SEARCHES_ALLOWED:
            return UseCaseResult[None](None, UserLimitsError())

        # 3. Validate user has not reached current plan limits
        if self._auth.current_user().plan_type != 'custom':
            plan = plans.get(self._auth.current_user().plan_type)

            if not plan.can_add_any_search(count_all_searches):
                return UseCaseResult[None](None, PlanLimitsError())

            count_active_searches = self._gateway.count_user_job_searches(
                user_id=self._auth.current_user().id,
                active_only=True
            )
            input.is_active = plan.can_add_active_search(count_active_searches)
            
        # 4. Attempt to create the job search and return it
        search = self._gateway.save_job_search(
            JobSearch(
                user_id=self._auth.current_user().id,
                name=input.name,
                is_active=input.is_active,
                location=input.location,
                search_parameters=jsonable_encoder(input.search_parameters),
                setting_send_email_notifications=input.setting_send_email_notifications,
                updated_at=datetime.now()
            )
        )
        return UseCaseResult[JobSearch](search)


response_model = JobSearchOutput


class JobSearchPresenter(JsonPresenter):
    
    def _present_success(self, result: UseCaseResult[JobSearch]) -> response_model:
        return result.result()