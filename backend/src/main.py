from fastapi import FastAPI

from src.job_search.job_search_controller import router

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

app.include_router(router)