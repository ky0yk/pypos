from sqlalchemy import (create_engine, Table, Column, Integer, String, ForeignKey, MetaData)
from sqlalchemy.sql import select

eng = create_engine(('postgresql://postgres:postgres@localhost:5432/postgres'))

with eng.connect() as con:

    meta = MetaData(eng)

    authors = Table('authors', meta, autoload=True)
    books = Table('books', meta, autoload=True)

    stm = select([authors.join(books)])
    rs = con.execute(stm)

    for row in rs:
        print(row['name'], row['title'])