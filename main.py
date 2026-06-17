from fastapi import FastAPI

app = FastAPI(
    title = "SaaS Project Management Platform",
    version  = "1.0.0"
)

projects = [
    {
        "id":1,
        "name":"Website redesign"
    },
    {
        "id":2,
        "name": "Rewamping the Portfolio"
    }
]


@app.get("/")
def health_check():
    return {
        "status":"Healthy"
    }
    
@app.get("/projects")
def get_projects():
    return projects



