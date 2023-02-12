from typing import List

from hale_sec.core.logging import log
from hale_sec.core.db.databasemodels import Filing


class FilingRepository:
    def __init__(self, db_session):
        self.db_session = db_session

    def add(self, item):
        log.debug("Adding filing %s", item.accessionNumber)
        self.db_session.add(item)

    def update(self, item: Filing):
        log.debug("Updating filing %s", item.id)
        self.db_session.merge(item)

    def remove(self, item: Filing):
        log.debug("Deleting filing %s", item.id)
        self.db_session.delete(item)

    def bulk_save(self, items: List[Filing]):
        self.db_session.bulk_save_objects(items)