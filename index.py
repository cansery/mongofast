from fastapi import FastAPI
from routes.user import user

description = """
First FASTAPI try by Sezer Ensari
"""

tags_metadata =[
    {
        "name": "User",
        "description": "Crud operations for users"
    }
]

app = FastAPI(
    title="FirstApp",
    description=description,
    contact= {
        "name": "Sezer Ensari",
        "url": "https://github.com/cansery"
    },
    openapi_tags=tags_metadata)
app.include_router(user, tags=["User"])

