from fastapi import FastAPI
from resultsapi.src.web.routes.result_routes import result_api

app = FastAPI()
app.include_router(result_api)
