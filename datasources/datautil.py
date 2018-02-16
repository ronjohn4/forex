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
        import pandas as pd
        # df = pandas.DataFrame(data, columns=['Fruit', 'Shop', 'Price'])
        # df.pivot(index='Fruit', columns='Shop', values='Price')

        df = pd.read_sql_query("SELECT collectiondate, quotecurrency, value FROM Pairs WHERE quotecurrency in ('EUR', 'AOA', 'AED', 'JPY', 'ZAR') ORDER by collectiondate;",
                               self.__conn)

        # df = pd.read_sql_query("SELECT collectiondate, quotecurrency, value FROM Pairs ORDER by collectiondate;",
        #                        self.__conn)

        data = []
        target = []

        data2 = []
        target2 = []

        cursor = self.__conn.execute(
            "SELECT collectiondate, quotecurrency, value FROM Pairs WHERE quotecurrency in ('EUR', 'AOA', 'AED', 'JPY', 'ZAR') ORDER by collectiondate;")
        rows = cursor.fetchall()
        for row in rows:
            print(row)
            data.append([row[0], row[1], row[2]])

        dp = df.pivot(index='collectiondate', columns='quotecurrency', values='value')
        # print('df')
        # print(df)

        # writer = pd.ExcelWriter('pandas_simple.xlsx', engine='xlsxwriter')
        # dp.to_excel(writer, "sheetx")
        # writer.save()

        # print('dp')
        # print(dp)
        #
        # print('dp-head')
        # print(dp.head())
        #
        # print('index')
        # print(dp.index)
        #
        # print('values')
        # print(dp.values)

        print('dp[2:7]')
        print(dp[2:7])

        p1 = dp[6:7]['AOA'].values
        print('dp[6:7]', p1)

        p2 = dp[7:8]['AOA'].values
        print('dp[7:8]', p2)

        print('diff:', p2-p1)

        data2.append(dp[2:7])
        target2.append(p2 > p1)

        data3 = []
        target3 = []
        for i in range(5):
            data3.append(dp[i:i+1].values)


        print('data3')
        print(data3)

        print('data:', data2)
        print('target:', target2)

        # dataset_array = data2.values


        # print('data:',type(data))
        # print('data2:',type(data2))
        # print('target:',type(target))
        # print('target2:',type(target2))



        return(data3, target2)
