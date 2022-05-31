from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

pg_user = "qenjyqdlmrnema"
pg_pwd = "5c9c2a97c3ff9195a11b7bacb71c5a6ee7ce9af93ca7506e68daec1f9676c8c6"
pg_port = "5432"
pg_db = "d33sv9ge9buo1q"
pg_host = "ec2-34-198-186-145.compute-1.amazonaws.com"
db_url = "postgresql+psycopg2://{username}:{password}@{host}:{port}/{db}".format(username=pg_user, password=pg_pwd,
                                                                                 host=pg_host, port=pg_port, db=pg_db)

SQLALCHEMY_DATABASE_URL = db_url

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={}, future=True
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine, future=True)

Base = declarative_base()


# DB Utilities

def getdb():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
