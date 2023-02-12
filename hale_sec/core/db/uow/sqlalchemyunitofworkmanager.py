from sqlalchemy.orm import sessionmaker

from hale_sec.core.db.uow.sqlalchemyunitofwork import SqlAlchemyUnitOfWork
from hale_sec.core.db.uow.unitofworkmanager import UnitOfWorkManager

class SqlAlchemyUnitOfWorkManager(UnitOfWorkManager):
    def __init__(self, db_engine):
        self.session_maker = sessionmaker(bind=db_engine, expire_on_commit=False)
    def start(self):
        return SqlAlchemyUnitOfWork(self.session_maker)