# LocalLens - Hyperlocal Civic Reporting

LocalLens is a hyperlocal civic reporting platform that allows citizens to report issues in their community, track reported issues, and view them in an interactive way.
The platform features an interactive interface with optional images and real-time updates.

---

## Tech Stack

- **Backend:** FastAPI, Supabase
- **Frontend:** Streamlit
- **Database:** Supabase Postgres
- **APIs:** Supabase REST & Realtime
- **Others:** Requests, Pydantic

---

## Folder Structure

```text

locallens/
│
├── backend/
│ ├── app/
│ │ ├── main.py # FastAPI app
│ │ ├── config.py # Supabase config
│ │ ├── models/
│ │ │ ├── issue.py # Pydantic models
│ │ └── ...
│ └── requirements.txt
│
├── frontend/
│ └── app.py # Streamlit frontend
│
└── README.md
```

---

## Setup Instructions

1. Clone & activate venv:
```bash
git clone <repo_url> && cd locallens
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
Install dependencies:
pip install -r requirements.txt
Configure Supabase (URL & Key in backend/app/config.py) and create issues table.
Run backend:
uvicorn app.main:app --reload --port 8000
Run frontend:
streamlit run frontend/app.py
Features
Submit issues with title, description, category, and optional image.
View all reported issues.
Filter issues by category and status.
Interactive frontend with auto-refresh.```
