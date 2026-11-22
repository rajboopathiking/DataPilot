from fastapi import FastAPI,HTTPException,status
from pydantic import BaseModel
from core import get_config,Config

from scalar_fastapi import get_scalar_api_reference
from fastapi.middleware.cors import CORSMiddleware
from db.session import close_db,check_connection
from contextlib import asynccontextmanager

@asynccontextmanager
async def lifespan(app : FastAPI):
    yield
    await close_db()

config = get_config()

app = FastAPI(
    title=config.app_name,
    swagger_ui_parameters={
        "filter":True,
    },
    redoc_url=None,
    docs_url=None,
    lifespan=lifespan

)

@app.get("/docs")
async def scalar_html():
    return get_scalar_api_reference(
        openapi_url=app.openapi_url,
        title=app.title,
        dark_mode=False,
        layout="classic",
   
    )

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
    allow_credentials=True
)

@app.get("/health",tags=["health"])
async def root():
    return {
        "Status":"Running",
        "application":config.app_name
    }

@app.get("/DBHealth",tags=["health"])
async def getDB_health():
    try:
        await check_connection()
        return {
            "DB":"postgres",
            "status":"live"
        }
    except Exception as e:
        raise HTTPException(status_code=500,details=f"sql Error : {e}")

if __name__ == "__main__":
    import uvicorn
    import asyncio
    conf = uvicorn.Config(
        app=app,
        host="127.0.0.1",
        port=8000,
        reload=True
    )

    server = uvicorn.Server(config=conf)
    asyncio.run(server.serve())
