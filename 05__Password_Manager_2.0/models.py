from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

# only execute this file when you want to create the table or
# if you update the model, and that update has to be reflected in the table(migration)

# for using MySQL as a Database install mysqlclient - pip install mysqlclient
# for using Postgres as a Database install psycopg2 - pip install psycopg2

# URI format 'database://user:pass@host/database'
URI = 'mysql://root:1234@localhost:3306/secrets'
engine = create_engine(URI,echo=False)
Base = declarative_base()

class Password(Base):
	__tablename__ = 'password'
	id = Column('id',Integer,primary_key=True)
	service = Column('service',String(25),nullable=False)
	text = Column('password',String(200),nullable=False)
	email = Column('email',String(30),nullable=True)


Base.metadata.create_all(engine)
