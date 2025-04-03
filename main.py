from fastapi import FastAPI
from routes import auth, tasks
from database import engine, Base

app = FastAPI()

# Create database tables
Base.metadata.create_all(bind=engine)

# Include authentication and task routes
app.include_router(auth.router)
app.include_router(tasks.router)

@app.get("/")
def read_root():
    return {"message": "Task Manager API is running!"}