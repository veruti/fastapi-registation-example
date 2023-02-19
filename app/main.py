from fastapi import FastAPI
from starlette.responses import RedirectResponse
from tortoise.contrib.fastapi import register_tortoise

from app.api.auth import auth_router
from app.config.db_config import DB_CONFIG

app = FastAPI(
    description="Registration example app"
)

register_tortoise(
    app=app,
    config=DB_CONFIG,
    generate_schemas=False,
)


@app.get("/", include_in_schema=False)
async def redirect_to_docs():
    return RedirectResponse(url="/docs")


app.include_router(router=auth_router, prefix="/auth")
