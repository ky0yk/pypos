from sqlalchemy import create_engine, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker, relationship

eng = create_engine(('postgresql://postgres:postgres@localhost:5432/postgres'))

Base = declarative_base()
 
class Author(Base):
    __tablename__ = "authors"
 
    authorid = Column(Integer, primary_key=True)
    name = Column(String)  
    books = relationship("Book")

class Book(Base):
    __tablename__ = "books"
 
    bookid = Column(Integer, primary_key=True)
    title = Column(String)      
    authorid = Column(Integer, ForeignKey("authors.authorid"))    
                           
    Author = relationship("Author")                           
         
Session = sessionmaker(bind=eng)
ses = Session()   

res = ses.query(Author).filter(Author.name=="Leo Tolstoy").first()

for book in res.books:
    print(book.title)

res = ses.query(Book).filter(Book.title=="Emma").first()    
print(res.Author.name)