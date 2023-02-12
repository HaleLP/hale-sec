from typing import List

from hale_sec.core.logging import log
from hale_sec.core.db.databasemodels import Person


class PersonRepository:
    def __init__(self, db_session):
        self.db_session = db_session

    def add(self, item):
        log.debug("Adding person %s", item.cik)
        self.db_session.add(item)

    def update(self, item: Person):
        log.debug("Updating person %s", item.id)
        self.db_session.merge(item)

    def remove(self, item: Person):
        log.debug("Deleting person %s", item.id)
        self.db_session.delete(item)

    def bulk_save(self, items: List[Person]):
        self.db_session.bulk_save_objects(items)