from sqlalchemy import create_engine,Column,Integer,String,ForeignKey
from sqlalchemy.orm import declarative_base,relationship,sessionmaker

Base=declarative_base()

class Author(Base):
    __tablename__='authors'
    id=Column(Integer,primary_key=True)
    name=Column(String)
    posts=relationship('Post', back_populates='author')

class Post(Base):
    __tablename__='posts'
    id=Column(Integer ,primary_key=True)
    name=Column(String)
    author_id=Column(Integer,ForeignKey('authors.id'))
    author=relationship('Author', back_populates='posts')


#Setting up the db
engine=create_engine('sqlite:///:memory')
Base.metadata.create_all(engine)
Session=sessionmaker(bind=engine)
session=Session()
#Createing the Author
author1=Author(name='John Doe')

#Creating User
post1=Post(name='How to always be mine',author=author1)
post2=Post(name='You dont know me yet',author =author1)



session.add_all([author1,post1,post2])
session.commit()

fetched_author=session.query(Author).filter_by(name='John Doe').first()
for post in fetched_author.posts:
    print(post.name)