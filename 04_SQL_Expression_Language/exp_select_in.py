from sqlalchemy import create_engine, Table, MetaData, tuple_
from sqlalchemy.sql import select

eng = create_engine(('postgresql://postgres:postgres@localhost:5432/postgres'))

with eng.connect() as con:

    meta = MetaData(eng)
    cars = Table('cars', meta, autoload=True)

    k = [(2,), (4, ), (6, ), (8,)]
    stm = select([cars]).where(tuple_(cars.c.id).in_(k))
    rs = con.execute(stm)

    for row in rs:
        print(row['id'], row['name'], row['price'])
