from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "mysql+mysqlconnector://root:password@127.0.0.1:3306/fivestars"

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False,autoflush=False,bind=engine)

Base = declarative_base()

######POSTGRES

## SQLALCHEMY_DATABASE_URL = os.environ.get('DATABASE_URL')
#####OR
# SQLALCHEMY_DATABASE_URL = ("postgresql://postgres_user:bF5WpzHgiJN9BBFUHKr7CzN1odv7Iw8A@dpg-cf788t94reb2e0bqrdtg-a:5432/postgres_fivestars")
#if SQLALCHEMY_DATABASE_URL.startswith('postgres://'):
  #  SQLALCHEMY_DATABASE_URL = SQLALCHEMY_DATABASE_URL.replace('postgres://','postgresql://',1)
