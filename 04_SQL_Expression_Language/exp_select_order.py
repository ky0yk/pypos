from sqlalchemy import create_engine, Table, MetaData
from sqlalchemy.sql import select, asc

eng = create_engine(('postgresql://postgres:postgres@localhost:5432/postgres'))

with eng.connect() as con:

    meta = MetaData(eng)
    cars = Table('cars', meta, autoload=True)

    stm = select([cars]).order_by(asc(cars.c.name))
    rs = con.execute(stm)

    for row in rs:
        print(row['id'], row['name'], row['price'])
