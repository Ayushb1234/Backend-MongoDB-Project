from fastapi import FastAPI
from app.routes import auth, challenge, progress

app = FastAPI()

app.include_router(auth.router)
app.include_router(challenge.router)
app.include_router(progress.router)