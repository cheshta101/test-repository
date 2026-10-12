
##models.py    → Database table

##mysql work
# from sqlalchemy import Column, Integer, String
# from database import Base

# class User(Base):                             
#     __tablename__ = "users"                     ##table name

#     id = Column(Integer, primary_key=True)      ##columns of the table
#     name = Column(String(100), nullable=False)
#     email = Column(String(100), nullable=False)
#     age = Column(Integer, nullable=False)


## postgresql work


from sqlalchemy import Column, Integer, String
from database import Base
from bson import ObjectId

# class User(Base):
#     __tablename__ = "student"

#     id = Column(Integer, primary_key=True, index=True)
#     name = Column(String, nullable=True)
#     email = Column(String, unique=True, nullable=True)
#     age = Column(Integer, nullable=True)


def serialize_user(user):
    return {
        "id": str(user["_id"]),
        "name": user.get("name"),
        "email": user.get("email"),
        "age": user.get("age")
    }    