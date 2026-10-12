
#### mysql connection start here
# from sqlalchemy import create_engine, text
# from sqlalchemy.orm import sessionmaker, declarative_base

# DATABASE_URL = "mysql+pymysql://root:cheshta@1233@localhost:3306/fastapi_practise_db"

# engine = create_engine(DATABASE_URL)


# try:
#     with engine.connect() as connection:
#         connection.execute(text("SELECT 1"))
#         print("Database connected successfully")
# except Exception as e:
#     print("Database connection failed:", e)


# SessionLocal = sessionmaker(
# #     autocommit=False,
# #     autoflush=False,
# #     bind=engine
# # )

# # Base = declarative_base()

# from sqlalchemy import create_engine, text
# from sqlalchemy.orm import sessionmaker, declarative_base



# DATABASE_URL = "mysql+pymysql://root:cheshta%40123@localhost:3306/fastapi_practise_db"

# engine = create_engine(DATABASE_URL)

# # try:
# #     with engine.connect() as connection:
# #         connection.execute(text("SELECT 1"))
# #         print("Database connected successfully")
# # except Exception as e:
# #     print("Database connection failedddd:", e)


# SessionLocal = sessionmaker(
#     autocommit=False,
#     autoflush=False,
#     bind=engine
# )

# Base = declarative_base()
# #### mysql connection end here


##postgresql start

# from sqlalchemy import create_engine , text
# from sqlalchemy.orm import sessionmaker, declarative_base

# DATABASE_URL = "postgresql+psycopg://postgres:cheshta%40123@localhost:5432/mylearningdb"


# engine = create_engine(
#     DATABASE_URL
#     # ,pool_pre_ping=True
    
# )


# try:
#     with engine.connect() as connection:
#         connection.execute(text("SELECT 1"))
#         print("Database connected successfully")
# except Exception as e:
#     print("Database connection failedddd:", e)


# SessionLocal = sessionmaker(
#     autocommit=False,
#     autoflush=False,
#     bind=engine
# )

# Base = declarative_base()


# def get_db():
#     db = SessionLocal()

#     try:
#         yield db
#     finally:
#         db.close()

  ##postgresql end


  # database.py
# database.py  for env file data
# import os
# from dotenv import load_dotenv
# from sqlalchemy import create_engine
# from sqlalchemy import create_engine , text
# from sqlalchemy.orm import sessionmaker, declarative_base

# load_dotenv()  # reads .env and loads into os.environ

# DB_USER = os.getenv("DB_USER")
# DB_PASSWORD = os.getenv("DB_PASSWORD")
# DB_HOST = os.getenv("DB_HOST")
# DB_PORT = os.getenv("DB_PORT")
# DB_NAME = os.getenv("DB_NAME")

# DATABASE_URL = f"postgresql+psycopg://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

# engine = create_engine(DATABASE_URL)
##postgre sql env file working check


## mongodb database code 
import os
from dotenv import load_dotenv
from pymongo import MongoClient
from sqlalchemy import create_engine
from sqlalchemy import create_engine , text
from sqlalchemy.orm import sessionmaker, declarative_base

# Load environment variables
load_dotenv()

# Get MongoDB connection string
MONGODB_URL = os.getenv("MONGODB_URL")

# Create MongoDB client
client = MongoClient(MONGODB_URL)

# Select database
db = client["fastapi_mongodb_db"]

# Select collection
users_collection = db["Users"]
## mongodb database code 

try:
    client.admin.command("ping")
    print("MongoDB connected successfullyyy!")

except Exception as e:
    print("MongoDB connection failed:", e)