from typing import Annotated
from fastapi import APIRouter, Depends, Body

from src.auth.services.auth_service import AuthService
from src.job_search.services.job_search_gateway import JobSearchGateway
from src.job_search.use_cases.list_job_searches import (
    ListJobSearchesUseCase,
    ListJobSearchesPresenter,
    response_model as list_job_searches_response
)
from src.job_search.use_cases.create_job_search import (
    NewJobSearch,
    CreateJobSearchUseCase,
    JobSearchPresenter,
    response_model as create_job_search_response
)


router = APIRouter()


AuthDep = Annotated[AuthService, Depends(AuthService.service)]

@router.get("/job_search", response_model=list_job_searches_response)
async def list_job_searches(auth: AuthDep, gateway: Annotated[JobSearchGateway, Depends()]):
    use_case = ListJobSearchesUseCase(
        gateway=gateway,
        auth=auth,
    )
    return ListJobSearchesPresenter().present(use_case.execute())

@router.post("/job_search", response_model=create_job_search_response)
async def create_job_search(input: Annotated[NewJobSearch, Body()], auth: AuthDep, gateway: Annotated[JobSearchGateway, Depends()]):
    use_case = CreateJobSearchUseCase(gateway=gateway, auth=auth)
    return JobSearchPresenter().present(use_case.execute(input))