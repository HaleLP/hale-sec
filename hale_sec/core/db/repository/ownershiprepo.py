from typing import List

from hale_sec.core.logging import log
from hale_sec.core.db.databasemodels import CompanyOwnership


class OwnershipRepository:
    def __init__(self, db_session):
        self.db_session = db_session

    def add(self, item):
        log.debug("Adding ownersip")
        self.db_session.add(item)

    def update(self, item: CompanyOwnership):
        log.debug("Updating ownership %s", item.id)
        self.db_session.merge(item)

    def remove(self, item: CompanyOwnership):
        log.debug("Deleting ownership %s", item.id)
        self.db_session.delete(item)

    def bulk_save(self, items: List[CompanyOwnership]):
        self.db_session.bulk_save_objects(items)