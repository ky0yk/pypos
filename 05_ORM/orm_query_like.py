from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

eng = create_engine(('postgresql://postgres:postgres@localhost:5432/postgres'))

Base = declarative_base()
Base.metadata.bind = eng

class Car(Base):
    __tablename__ = "Cars"

    Id = Column(Integer, primary_key=True)
    Name = Column(String)
    Price = Column(Integer)

Session = sessionmaker(bind=eng)
ses = Session()

rs = ses.query(Car).filter(Car.Name.like('%en'))

for car in rs:
    print(car.Name, car.Price)