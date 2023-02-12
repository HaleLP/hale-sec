from sqlalchemy import create_engine
from sqlalchemy.engine.url import URL 

from hale_sec.core.config import Config
from hale_sec.core.logging import log


def get_db_engine(config: Config):
    connection_uri = URL.create(
        "mysql+pymysql",
        username=config.db_user,
        password=config.db_password,
        host=config.db_host,
        database=config.db_name,
    )
    return create_engine(connection_uri, echo=False, pool_size=config.db_pool_size, pool_pre_ping=True)
    