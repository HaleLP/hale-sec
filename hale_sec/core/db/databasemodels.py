from sqlalchemy import Column, Integer, String, DateTime, Date, func, Boolean, Text, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class Filing(Base):

    __tablename__ = 'sec_filing'

    id = Column(Integer, primary_key=True)
    accessionNumber = Column(String(50), nullable=False)
    url = Column(String(250))
    fullSubmissionUrl = Column(String(250))
    filingDetailsUrl = Column(String(250))
    filingDetailsFilename = Column(String(250))
    type = Column(String(50))
    periodOfReport = Column(String(15))
    filedDate = Column(String(15))
    changeDate = Column(String(15))


class Company(Base):

    __tablename__ = 'sec_company'

    id = Column(Integer, primary_key=True)
    cik = Column(Integer, nullable=False, unique=True)
    classification = Column(String(150))
    irsNumber = Column(Integer)
    stateOfIncorporation = Column(String(25))
    street1 = Column(String(250))
    street2 = Column(String(250))
    city = Column(String(250))
    zip = Column(String(25))
    state = Column(String(50))
    phone = Column(String(50))


class Person(Base):

    __tablename__ = 'sec_person'

    id = Column(Integer, primary_key=True)
    cik = Column(Integer, nullable=False, unique=True)
    name = Column(String(250))
    street1 = Column(String(250))
    street2 = Column(String(250))
    city = Column(String(250))
    zip = Column(String(25))
    state = Column(String(50))


class CompanyOwnership(Base):

    __tablename__ = 'sec_company_ownership'

    id = Column(Integer, primary_key=True)
    company_cik = Column(Integer, nullable=False, unique=True)
    owner_cik = Column(Integer, nullable=False, unique=True)
    securitiesOwned = Column(Integer)
    isDirector = Column(Boolean)
    isOfficer = Column(Boolean)
    isTenPercentOwner = Column(Boolean)
    isOther = Column(Boolean)
    officerTitle = Column(String(150))
    date = Column(Date)


class NonDerivative(Base):

    __tablename__ = 'sec_non_derivative'

    id = Column(Integer, primary_key=True)
    company_cik = Column(Integer, nullable=False, unique=True)
    owner_cik = Column(Integer, nullable=False, unique=True)
    securityTitle = Column(String(150))
    securityValue = Column(String(150))
    directOrIndirect = Column(String(25))
    date = Column(Date)


class Derivative(Base):

    __tablename__ = 'sec_derivative'

    id = Column(Integer, primary_key=True)
    company_cik = Column(Integer, nullable=False, unique=True)
    owner_cik = Column(Integer, nullable=False, unique=True)
    securityTitle = Column(String(150))
    conversionOrExercisePrice = Column(String(150))
    exerciseDate = Column(String(25))
    expirationDate = Column(String(25))
    underlyingSecurityTitle = Column(String(150))
    underlyingSecurityShares = Column(String(150))
    directOrIndirect = Column(String(25))
    date = Column(Date)
