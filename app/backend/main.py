from fastapi import FastAPI
from product.routes import product_router
from starlette.middleware.cors import CORSMiddleware
from config import config

api_path = f"/api/{config.API_VERSION}"

app = FastAPI(
    title="SegundaMano",
    description="""
    App where you can sell objects that you don't use or you can 
    buy it from other persons.
    """,
    version="0.1",
    openapi_url=f"{api_path}/openapi.json",
    docs_url=f"{api_path}/docs",
    redoc_url=None
)

origins = [
    'http://localhost:8000',
    'http://localhost:8080'
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)


@app.on_event('startup')
async def app_startup():
    config.load_config()


@app.on_event('shutdown')
async def app_shutdown():
    config.close_db_client()


app.include_router(
    product_router,
    prefix='/products',
    tags=['products'],
    responses={404: {'description': 'not found'}},
)
