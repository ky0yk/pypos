from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

eng = create_engine(('postgresql://postgres:postgres@localhost:5432/postgres'))

Base = declarative_base()

class Car(Base):
    __tablename__ = "Cars"

    Id = Column(Integer, primary_key=True)
    Name = Column(String)
    Price = Column(Integer)

Session = sessionmaker(bind=eng)
ses = Session()

rs = ses.query(Car).filter(Car.Id.in_([2, 4, 6, 8]))

for car in rs:
    print(car.Id, car.Name, car.Price)