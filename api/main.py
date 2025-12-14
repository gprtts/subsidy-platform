from fastapi import FastAPI
from api.routes import router

app = FastAPI(title="Subsidy Platform API")
app.include_router(router)
