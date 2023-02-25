from sqlalchemy import create_engine, inspect

eng = create_engine(('postgresql://postgres:postgres@localhost:5432/postgres'))

insp = inspect(eng)
print(insp.get_table_names())
print(insp.get_columns("cars"))
# print (insp.get_primary_keys("cars")) // deprecatedになっていた
print(insp.get_schema_names())