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

1. Clone & activate virtual environment
git clone <repo_url> && cd locallens
python -m venv venv
venv\Scripts\activate

2. Install dependencies
pip install -r requirements.txt

3. Configure Supabase
Set URL & Key in backend/app/config.py and create 'issues' table

 4. Run backend
uvicorn app.main:app --reload --port 8000

 5. Run frontend
streamlit run frontend/app.py
