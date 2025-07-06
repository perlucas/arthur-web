from fastapi import APIRouter, Depends

from src.auth.services.auth_service import AuthService
from src.job_search.services.job_search_gateway import JobSearchGateway
from src.job_search.use_cases.list_job_searches import (
    ListJobSearchesUseCase,
    ListJobSearchesPresenter,
    response_model as list_job_searches_response
)
from typing import Annotated


router = APIRouter()


AuthDep = Annotated[AuthService, Depends(AuthService.service)]

@router.get("/job_search", response_model=list_job_searches_response)
async def list_job_searches(auth: AuthDep, gateway: Annotated[JobSearchGateway, Depends()]):
    use_case = ListJobSearchesUseCase(
        gateway=gateway,
        auth=auth,
    )
    return ListJobSearchesPresenter().present(use_case.execute())