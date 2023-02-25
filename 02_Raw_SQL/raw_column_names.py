from sqlalchemy import create_engine
from sqlalchemy.sql import text

eng = create_engine(('postgresql://postgres:postgres@localhost:5432/postgres'))

with eng.connect() as con:

    con.execute(text('''CREATE TABLE Cars(Id INTEGER PRIMARY KEY,
        Name TEXT, Price INTEGER)'''))
    rs = con.execute(text('SELECT * FROM Cars'))

    print(rs.keys())