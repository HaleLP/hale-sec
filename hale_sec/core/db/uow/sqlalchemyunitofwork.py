from sqlalchemy.orm import scoped_session

from hale_sec.core.db.uow.unitofwork import UnitOfWork

from hale_sec.core.db.repository.companyrepo import CompanyRepository
from hale_sec.core.db.repository.derivativerepo import DerivativeRepository
from hale_sec.core.db.repository.filingrepo import FilingRepository
from hale_sec.core.db.repository.nonderivativerepo import NonDerivativeRepository
from hale_sec.core.db.repository.ownershiprepo import OwnershipRepository
from hale_sec.core.db.repository.personrepo import PersonRepository


class SqlAlchemyUnitOfWork(UnitOfWork):

    def __init__(self, session_factory):
        self.session_factory = scoped_session(session_factory)

    def __enter__(self):
        self.session = self.session_factory()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.session.close()

    def commit(self):
        self.session.commit()

    def rollback(self):
        self.session.rollback()

    @property
    def company(self) -> CompanyRepository:
        return CompanyRepository(self.session)

    @property
    def derivative(self) -> DerivativeRepository:
        return DerivativeRepository(self.session)

    @property
    def filing(self) -> FilingRepository:
        return FilingRepository(self.session)

    @property
    def nonderivative(self) -> NonDerivativeRepository:
        return NonDerivativeRepository(self.session)

    @property
    def ownership(self) -> OwnershipRepository:
        return OwnershipRepository(self.session)

    @property
    def person(self) -> PersonRepository:
        return PersonRepository(self.session)
