from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, MetaData, Table
import sqlite3


Base = declarative_base()


class Pairs(Base):
    __tablename__ = 'Pairs'
    id = Column(Integer, primary_key=True)
    collectiondate = Column(String())
    collectiontime = Column(String())
    countercurrency = Column(String(3))
    quotecurrency = Column(String(3))
    value = Column(Integer)
    predictvalue = Column(Integer)


class forexDB():
    __pairs = None
    __engine = None
    __conn = None

    def __init__(self):
        # Create an engine that stores data in the local directory's
        # sqlalchemy_example.db file.
        self.__conn = sqlite3.connect('forex.db')

        self.__engine = create_engine('sqlite:///forex.db')

        # Create all tables in the engine. This is equivalent to "Create Table"
        # statements in raw SQL.
        Base.metadata.create_all(self.__engine)

        self.__engine.echo = False
        metadata = MetaData(self.__engine)
        self.__pairs = Table('Pairs', metadata, autoload=True)


    def date_already_saved(self, checkdate):
        cursor = self.__conn.execute("select * from Pairs where collectiondate='{0}';".format(checkdate))
        return cursor.fetchone() is not None


    def add_pair(self, collectiondate, collectiontime, countercurrency, quotecurrency, value):
        i = self.__pairs.insert()
        i.execute(collectiondate=collectiondate,
                  collectiontime=collectiontime,
                  countercurrency=countercurrency,
                  quotecurrency=quotecurrency,
                  value=value)

    def return_training_data(self):
        data = []
        target = []
        cursor = self.__conn.execute(
            "select value from Pairs where quotecurrency='{0}' order by collectiondate;".format('EUR'))
        rows = cursor.fetchall()
        for row in rows:
            print(row)
            data.append(row[0])
        print('data:', data)
        print('target:', target)
        return(data, target)