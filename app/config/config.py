from motor.motor_asyncio import AsyncIOMotorClient
import yaml


def load_config() -> dict:
    with open('config/config.yml') as yaml_file:
        conf = yaml.load(yaml_file.read(), Loader=yaml.SafeLoader)
    return conf


CONF = load_config()


DB_CLIENT = AsyncIOMotorClient(
    host=CONF.get('databases', dict())['default']['HOST'],
    port=CONF.get('databases', dict())['default']['PORT'],
    username=CONF.get('databases', dict())['default']['USER'],
    password=CONF.get('databases', dict())['default']['PASSWORD']
)


DB = DB_CLIENT[CONF.get('databases', dict)['default']['NAME']]


def close_db_client():
    DB_CLIENT.close()
