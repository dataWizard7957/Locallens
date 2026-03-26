from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from app.config import supabase
from app.models.issue import IssueCreate, IssueUpdate, IssueOut
from uuid import uuid4
from datetime import datetime

app = FastAPI(title="LocalLens MVP")

# CORS (optional for frontend)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # or your frontend URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/issues", response_model=list[IssueOut])
def get_issues():
    try:
        result = supabase.table("issues").select("*").execute()
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Supabase error: {str(e)}")
    
    if hasattr(result, "error") and result.error:
        raise HTTPException(status_code=500, detail=f"Supabase error: {result.error}")
    
    # return empty list if no issues
    return result.data or []

@app.post("/issues", response_model=IssueOut)
def create_issue(issue: IssueCreate):
    new_issue = {
        "id": str(uuid4()),
        "title": issue.title,
        "description": issue.description,
        "category": issue.category,
        "image_url": issue.image_url or "",
        "status": "reported",
        "created_at": datetime.utcnow().isoformat()
    }
    result = supabase.table("issues").insert(new_issue).execute()
    if hasattr(result, "error") and result.error:
        raise HTTPException(status_code=500, detail=str(result.error))
    return new_issue

@app.patch("/issues/{issue_id}", response_model=IssueOut)
def update_issue(issue_id: str, update: IssueUpdate):
    result = supabase.table("issues").update({"status": update.status}).eq("id", issue_id).execute()
    if hasattr(result, "error") and result.error:
        raise HTTPException(status_code=500, detail=str(result.error))
    if not result.data:
        raise HTTPException(status_code=404, detail="Issue not found")
    return result.data[0]
