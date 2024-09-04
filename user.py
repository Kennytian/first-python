from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base
from dotenv import load_dotenv
import os

load_dotenv()

database_url = os.getenv("DATABASE_URL")

api_key = os.getenv("NAME")
print(f"API Key is: {api_key}")

engine = create_engine(database_url)
Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String)
    age = Column(Integer)


# SELECT QUERY 1
print("SELECT QUERY 1")
users = session.query(User).all()
for user in users:
    print(user.id, user.name, user.email, user.age)

# SELECT QUERY 2
print("SELECT QUERY 2")
users = session.query(User.id, User.name).all()
for user in users:
    print(user.id, user.name)

# ORDER BY
print("ORDER BY")
users = session.query(User).order_by(User.age).all()
for user in users:
    print(user.id, user.name, user.email, user.age)

# DISTINCT
print("DISTINCT")
users = session.query(User.age).distinct().all()
for user in users:
    print(user.age)

# WHERE
print("WHERE")
users = session.query(User).filter(User.age > 30).all()
for user in users:
    print(user.id, user.name, user.email, user.age)
