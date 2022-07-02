from sqlalchemy import Integer, String
from sqlalchemy.sql.schema import Column

from ..db_setup import Base


class Interests(Base):
    __tablename__ = 'interests'

    id = Column(Integer, primary_key=True)
    title = Column(String(256))
    interest_code = Column(String(50))
    job_zone = Column(Integer)
    description = Column(String(1000))
    abilities = Column(String(1200))
    skills = Column(String(1000))
    sector = Column(String(50))
