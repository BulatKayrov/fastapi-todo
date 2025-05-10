import logging

import uvicorn
from fastapi import FastAPI

from api import router
from core.config import configure_logging

log = logging.getLogger(__name__)
app = FastAPI()
app.include_router(router)
configure_logging()


@app.get("/")
async def root():
    log.info("Root request")
    return {"message": "Hello World"}


if __name__ == "__main__":
    uvicorn.run(app="main:app", reload=True, host="0.0.0.0", port=8000)
