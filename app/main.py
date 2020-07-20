from fastapi import FastAPI
from .products.routes import product_router
from .config import config

app = FastAPI()


app.include_router(
    product_router,
    prefix='/products',
    tags=['products'],
    responses={404: {'description': 'not found'}},
)


@app.on_event('startup')
async def app_startup():
    config.load_config()


@app.on_event('shutdown')
async def app_shutdown():
    config.close_db_client()
