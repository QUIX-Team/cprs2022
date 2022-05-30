from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

pg_user = "hagpcmgspnvkcr"
pg_pwd = "46491ae6f81d4ba8e58e2de8adf69234b409cb80eaf3e8505e96b396eabae7a4"
pg_port = "5432"
pg_db = "d8auiotjh57a3q"
pg_host = "ec2-34-230-153-41.compute-1.amazonaws.com"
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
