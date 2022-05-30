from sqlalchemy import Integer, String, Boolean, FLOAT
from sqlalchemy.sql.schema import Column

from ..db_setup import Base


class Interests(Base):
    __tablename__ = 'courses'

    id = Column(Integer, primary_key=True)
    title = Column(String(512))
    url = Column(String(512))
    is_paid = Column(Boolean)
    num_subscribers = Column(Integer)
    avg_rating = Column(FLOAT)
    avg_rating_recent = Column(FLOAT)
    rating = Column(FLOAT)
    num_reviews = Column(Integer)
    num_published_lectures = Column(Integer)
    field = Column(String(256))
