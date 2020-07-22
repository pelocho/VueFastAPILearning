from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from product.routes import product_router
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

templates = Jinja2Templates(directory="templates")

app.mount("/static", StaticFiles(directory="static"), name="static")

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


@app.get('/')
async def homepage(request: Request):
    return templates.TemplateResponse('home.html', {'request': request})
