from fastapi import FastAPI
from contextlib import asynccontextmanager
import uvicorn
from loguru import logger

@asynccontextmanager
async def lifespan(_: FastAPI):
    logger.info("FastAPI application starting up")
    yield
    logger.info("FastAPI application shutting down")


app = FastAPI(lifespan=lifespan)


@app.get("/ping")
async def ping():
    logger.info("Ping endpoint called")
    return {"message": "pong"}


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)