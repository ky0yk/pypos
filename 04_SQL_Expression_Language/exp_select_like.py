from sqlalchemy import create_engine, Table, MetaData
from sqlalchemy.sql import select

eng = create_engine(('postgresql://postgres:postgres@localhost:5432/postgres'))

with eng.connect() as con:

    meta = MetaData(eng)
    cars = Table('cars', meta, autoload=True)

    stm = select([cars]).where(cars.c.name.like('%en'))
    rs = con.execute(stm)

    print(rs.fetchall())