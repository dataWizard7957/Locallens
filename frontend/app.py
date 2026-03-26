import streamlit as st 
import requests

# ------------------------
# Config
# ------------------------
BACKEND_URL = "http://127.0.0.1:8000"  

# ------------------------
# Helper functions
# ------------------------
@st.cache_data
def get_issues():
    try:
        response = requests.get(f"{BACKEND_URL}/issues")
        response.raise_for_status()
        return response.json()
    except Exception as e:
        st.error(f"Error fetching issues: {e}")
        return []

def submit_issue(title, description, category, image_url):
    payload = {
        "title": title,
        "description": description,
        "category": category,
        "image_url": image_url,
    }
    try:
        response = requests.post(f"{BACKEND_URL}/issues", json=payload)
        response.raise_for_status()
        return True
    except Exception as e:
        st.error(f"Error submitting issue: {e}")
        return False

# ------------------------
# Streamlit App
# ------------------------
st.set_page_config(page_title="LocalLens", page_icon="🌆", layout="wide")

st.sidebar.title("Navigate")
page = st.sidebar.radio("Go to", ["Home", "Reported Issues", "Report an Issue"])

# ------------------------
# HOME PAGE
# ------------------------
if page == "Home":
    st.title("🌆 LocalLens - Hyperlocal Civic Reporting")
    st.markdown(
        """
        Welcome to **LocalLens**, your hyperlocal platform for reporting civic issues.
        Use the sidebar to navigate between pages:
        - **Reported Issues**: See all issues reported by the community.
        - **Report an Issue**: Submit a new issue with details and an optional image.
        """
    )

# ------------------------
# REPORTED ISSUES PAGE
# ------------------------
elif page == "Reported Issues":
    st.title("Reported Issues")
    issues = get_issues()

    if not issues:
        st.info("No issues reported yet.")
    else:
        # Optional filters
        categories = list(set([issue["category"] for issue in issues]))
        statuses = list(set([issue["status"] for issue in issues]))
        selected_category = st.selectbox("Filter by Category", ["All"] + categories)
        selected_status = st.selectbox("Filter by Status", ["All"] + statuses)

        filtered = issues
        if selected_category != "All":
            filtered = [i for i in filtered if i["category"] == selected_category]
        if selected_status != "All":
            filtered = [i for i in filtered if i["status"] == selected_status]

        for issue in filtered:
            st.markdown("---")
            st.subheader(issue["title"])
            st.write(f"**Category:** {issue['category']}")
            st.write(f"**Status:** {issue['status']}")
            st.write(issue["description"])
            if issue.get("image_url"):
                st.image(issue["image_url"], use_column_width=True)
        st.markdown("---")

# ------------------------
# REPORT AN ISSUE PAGE
# ------------------------
elif page == "Report an Issue":
    st.title("Report an Issue")

    with st.form("issue_form"):
        title = st.text_input("Title")
        description = st.text_area("Description")
        category = st.selectbox("Category", ["Road", "Garbage", "Water", "Electricity", "Other"])
        image_url = st.text_input("Image URL (optional)")
        submitted = st.form_submit_button("Submit Issue")

        if submitted:
            if not title or not description:
                st.warning("Title and Description are required!")
            else:
                success = submit_issue(title, description, category, image_url)
                if success:
                    st.success("Issue submitted successfully!")
                    st.experimental_rerun()  
