from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base, relationship, sessionmaker

Base = declarative_base()

class Author(Base):
    __tablename__ = 'authors'  # ✅ changed table name to match class meaning
    id = Column(Integer, primary_key=True)
    name = Column(String)
    posts = relationship('Post', back_populates='author')  # ✅ back_populates must match

class Post(Base):
    __tablename__ = 'posts'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    author_id = Column(Integer, ForeignKey('authors.id'))  # ✅ match Author's table name
    author = relationship('Author', back_populates='posts')  # ✅ match Author.posts

# Setup
engine = create_engine('sqlite:///:memory:')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

# Create author and posts
author1 = Author(name='John Doe')
post1 = Post(name='How to always be mine', author=author1)
post2 = Post(name="You don't know me yet", author=author1)

session.add_all([author1, post1, post2])
session.commit()

# Fetch and print posts by author
fetched_author = session.query(Author).filter_by(name='John Doe').first()
for post in fetched_author.posts:
    print(post.name)
