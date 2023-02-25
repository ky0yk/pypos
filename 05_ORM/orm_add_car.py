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

c1 = Car(Name='Oldsmobile', Price=23450)
ses.add(c1)
ses.commit()

rs = ses.query(Car).all()

for car in rs:
    print(car.Name, car.Price)