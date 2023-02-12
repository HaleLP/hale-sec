from typing import List

from hale_sec.core.logging import log
from hale_sec.core.db.databasemodels import NonDerivative


class NonDerivativeRepository:
    def __init__(self, db_session):
        self.db_session = db_session

    def add(self, item):
        log.debug("Adding NonDerivative")
        self.db_session.add(item)

    def update(self, item: NonDerivative):
        log.debug("Updating NonDerivative %s", item.id)
        self.db_session.merge(item)

    def remove(self, item: NonDerivative):
        log.debug("Deleting NonDerivative %s", item.id)
        self.db_session.delete(item)

    def bulk_save(self, items: List[NonDerivative]):
        self.db_session.bulk_save_objects(items)