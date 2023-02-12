from celery import Task

from hale_sec.core import logging
from hale_sec.core.config import Config
from hale_sec.core.db.db_utils import get_db_engine
from hale_sec.core.db.uow.sqlalchemyunitofworkmanager import SqlAlchemyUnitOfWorkManager


class SqlAlchemyTask(Task):
    def __init__(self):
        self.config = Config()
        self.uowm = SqlAlchemyUnitOfWorkManager(get_db_engine(self.config))
        
