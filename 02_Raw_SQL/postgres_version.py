from sqlalchemy import create_engine

eng = create_engine(('postgresql://postgres:postgres@localhost:5432/postgres'))
con = eng.connect()

rs = con.execute("SELECT VERSION()")
print (rs.fetchone())

con.close()