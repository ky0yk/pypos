from sqlalchemy import (create_engine, Table, Column, Integer, String, MetaData)
from sqlalchemy.sql import select

eng = create_engine(('postgresql://postgres:postgres@localhost:5432/postgres'))

with eng.connect() as con:

    meta = MetaData(eng)
    cars = Table('cars', meta,
        Column('Id', Integer, primary_key=True),
        Column('Name', String),
        Column('Price', Integer)
    )

    cars.create()
    
    ins1 = cars.insert().values(Id=1, Name='Audi', Price=52642)
    con.execute(ins1)

    ins2 = cars.insert().values(Id=2, Name='Mercedes', Price=57127)
    con.execute(ins2)

    ins3 = cars.insert().values(Id=3, Name='Skoda', Price=6000)
    con.execute(ins3)

    stm = select([cars])
    rs = con.execute(stm)

    for row in rs:
        print(row['Id'], row['Name'], row['Price'])
