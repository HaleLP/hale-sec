from typing import List

from hale_sec.core.logging import log
from hale_sec.core.db.databasemodels import Company


class CompanyRepository:
    def __init__(self, db_session):
        self.db_session = db_session

    def add(self, item):
        log.debug("Adding company %s", item.cik)
        self.db_session.add(item)

    def update(self, item: Company):
        log.debug("Updating company %s", item.id)
        self.db_session.merge(item)

    def remove(self, item: Company):
        log.debug("Deleting company %s", item.id)
        self.db_session.delete(item)

    def bulk_save(self, items: List[Company]):
        self.db_session.bulk_save_objects(items)