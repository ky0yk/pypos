from sqlalchemy import (create_engine, Table, Column, Integer, String, MetaData)

eng = create_engine(('postgresql://postgres:postgres@localhost:5432/postgres'))

meta = MetaData()
meta.reflect(bind=eng)

for table in meta.tables:
    print(table)
