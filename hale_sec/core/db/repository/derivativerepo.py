from typing import List

from hale_sec.core.logging import log
from hale_sec.core.db.databasemodels import Derivative


class DerivativeRepository:
    def __init__(self, db_session):
        self.db_session = db_session

    def add(self, item):
        log.debug("Adding derivative %s", item.id)
        self.db_session.add(item)

    def update(self, item: Derivative):
        log.debug("Updating derivative %s", item.id)
        self.db_session.merge(item)

    def remove(self, item: Derivative):
        log.debug("Deleting derivative %s", item.id)
        self.db_session.delete(item)

    def bulk_save(self, items: List[Derivative]):
        self.db_session.bulk_save_objects(items)

    def get_by_id(self, id: int) -> Derivative:
        return self.db_session.query(Derivative).filter(Derivative.id == id).first()

    def get_all_by_company_cik(self, company_cik: int, limit: int = None) -> List[Derivative]:
        return self.db_session.query(Derivative).filter(Derivative.company_cik == company_cik).order_by(Derivative.id).limit(limit).all()
    
    def get_all_by_owner_cik(self, owner_cik: int, limit: int = None) -> List[Derivative]:
        return self.db_session.query(Derivative).filter(Derivative.owner_cik == owner_cik).order_by(Derivative.id).limit(limit).all()


