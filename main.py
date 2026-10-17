from fastapi import FastAPI, Header, HTTPException
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

class JobsListResponseItem(BaseModel):
    job_id: str
    status : str
    progress : int
    output_url : Optional[str] = None

class JobsPage(BaseModel):
    items: Optional[list[JobsListResponseItem]] = None
    total: int

class CreateJobRequest(BaseModel):
    input_url: str
    template_id: Optional[str] = None



@app.get("/jobs")
def list_jobs(
    limit: int = 10, 
    auth : str | None = Header(None)
):

    if auth != "secret":
        raise HTTPException(status_code=401, detail="Unauthorized")

    all_items = [
        JobsListResponseItem(job_id="abc-123", status="done", progress=100, output_url="https://example.com"),
        JobsListResponseItem(job_id="def-456", status="running", progress=45),
        JobsListResponseItem(job_id="ghi-789", status="pending", progress=0),
    ]
    items = all_items[:limit]

    return JobsPage(items = items,total=len(all_items))


@app.post("/jobs")
def create_job(
    request: CreateJobRequest,
    auth : str | None = Header(None)
):
    if auth != "secret":
        raise HTTPException(status_code=401, detail="Unauthorized")

    

    new_job = JobsListResponseItem(
        job_id="new-001", 
        status="pending", 
        progress=0
    )

    return new_job

