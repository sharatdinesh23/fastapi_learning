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
    },
    {
        "id":3,
        "name": "this is my project"
    }
]

users = [
    {
        "id":1,
        "name":"Sharath"
    },
    {
        "id":2,
        "name":"Darshan"
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

@app.get("/users",description="This url is for accessing the user",tags=["user"])
def get_user():
    return users


