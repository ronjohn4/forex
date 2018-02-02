from sqlalchemy import Column, Integer, String, Date, Time
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, MetaData, Table
from sqlalchemy.orm import sessionmaker


Base = declarative_base()


class Pairs(Base):
    __tablename__ = 'Pairs'
    id = Column(Integer, primary_key=True)
    collectiondate = Column(String(), nullable=True)
    collectiontime = Column(String(), nullable=True)
    countercurrency = Column(String(3), nullable=False)
    quotecurrency = Column(String(3), nullable=False)
    value = Column(Integer, nullable=False)


class forexDB():
    __pairs = None
    __engine = None

    def __init__(self):
        # Create an engine that stores data in the local directory's
        # sqlalchemy_example.db file.
        self.__engine = create_engine('sqlite:///forex.db')

        # Create all tables in the engine. This is equivalent to "Create Table"
        # statements in raw SQL.
        Base.metadata.create_all(self.__engine)

        self.__engine.echo = False
        metadata = MetaData(self.__engine)
        self.__pairs = Table('Pairs', metadata, autoload=True)


    def date_already_saved(self, checkdate):
        import sqlite3
        conn = sqlite3.connect('forex.db')
        cursor = conn.execute("select * from Pairs where collectiondate='{0}';".format(checkdate))
        return cursor.fetchone() is not None


    def add_pair(self, collectiondate, collectiontime, countercurrency, quotecurrency, value):
        i = self.__pairs.insert()
        i.execute(collectiondate=collectiondate,
                  collectiontime=collectiontime,
                  countercurrency=countercurrency,
                  quotecurrency=quotecurrency,
                  value=value)

