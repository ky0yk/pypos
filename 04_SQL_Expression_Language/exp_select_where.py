from sqlalchemy import create_engine, Table, MetaData
from sqlalchemy.sql import select, and_

eng = create_engine(('postgresql://postgres:postgres@localhost:5432/postgres'))

with eng.connect() as con:

    meta = MetaData(eng)
    cars = Table('cars', meta, autoload=True)

    stm = select([cars]).where(and_(cars.c.price > 10000,
        cars.c.price < 40000))

    rs = con.execute(stm)

    print(rs.fetchall())