# from fastapi import FastAPI,Depends
# from sqlalchemy.orm import Session
# from database import engine , Base,SessionLocal
# from sqlalchemy import text    ##sirf isliye chahiye kyunki hum SELECT 1 jaisi raw SQL query chala rahe hain.
# ##from sqlalchemy import text isliye use kiya kyunki hum SQL query directly execute kar rahe hain.

# from models import User
# from schemas import UserCreate



# app=FastAPI()

# # Create database tables
# Base.metadata.create_all(bind=engine)


# # Database Session
# def get_db():
#     db = SessionLocal()

#     try:
#         yield db
#     finally:
#         db.close()

# @app.get('/')
# def home():
#     return{'message':'hello'}

# @app.get("/test-db")
# def test_db():
#     with engine.connect() as connection:
#         connection.execute(text("SELECT 1"))

#     return {"message": "Database connected successfully"}

# ##post api after db connection
# @app.post("/users")
# def create_user(user: UserCreate, db: Session = Depends(get_db)):  ##Why do we use it in POST? UserCreate in post? read below
#     ## The data coming in the request body should be validated according to the UserCreate schema.

#     new_user = User(
#         name=user.name,
#         email=user.email,
#         age=user.age
#     )

#     db.add(new_user)
#     db.commit()
#     db.refresh(new_user)

#     return new_user


#     ## ab get user bnao jo post api se data add kra hai db mein ab get krke dekhenge
# @app.get("/users")              ##all users ka data access krne ka code or endpoint
# def get_users(db: Session = Depends(get_db)):   ## db:session = Yahan hum FastAPI ko bata rahe hain:

# ##Mujhe database ke saath kaam karne ke liye SQLAlchemy ka Session chahiye.yhi db:session ka mtlb hota hai or depends(get_db) ka mtlb hota hai ki get_db function ko call karke mujhe db session provide karo. Ask FastAPI to provide the DB session
#     users = db.query(User).all()

#     return users


# ##single user id rehta hai isme, simple hai vo bhi,fastapi -;earning wale mein dekh lena usme hai



# # #postgresql

# from fastapi import FastAPI, Depends
# from sqlalchemy.orm import Session
# # from database import engine, Base        ##used fo mysql and postgresql
# from database import users_collection ##used for mongodb

# import models

# from database import engine, Base, get_db
# from models import User
# from schemas import UserCreate, UserUpdate,UserPatch
# from sqlalchemy import text
# from fastapi import Depends
# app = FastAPI()

# Base.metadata.create_all(bind=engine)


# @app.get("/")
# def home():
#     return {"message": "FastAPI is running"}



# # to check connection with db
# @app.get("/test-db")
# def test_db():
#     with engine.connect() as connection:
#         connection.execute(text("SELECT 1"))

#     return {"message": "Database connected successfully"}





# ## get api via postgresql
# # GET all users
# @app.get("/users")
# def get_users(db: Session = Depends(get_db)):
#     users = db.query(User).all()

#     return users


# # POST new user with postgresql


# @app.post("/users")
# def create_user(user: UserCreate, db: Session = Depends(get_db)):

#     new_user = User(
#         name=user.name,
#         email=user.email,
#         age=user.age
#     )

#     db.add(new_user)
#     db.commit()
#     db.refresh(new_user)

#     return new_user



# #put new user in postgresql
# # PUT
# @app.put("/users/{user_id}")
# def update_user(
#     user_id: int,
#     user: UserUpdate,
#     db: Session = Depends(get_db)
# ):

#     existing_user = db.query(User).filter(User.id == user_id).first()

#     if existing_user is None:
#         raise HTTPException(
#             status_code=404,
#             detail="User not found"
#         )

#     existing_user.name = user.name
#     existing_user.email = user.email
#     existing_user.age = user.age

#     db.commit()
#     db.refresh(existing_user)

#     return existing_user



# ##patch api posetgresql

# # @app.patch("/users/{user_id}")
# # def patch_user(
# #     user_id: int,
# #     user: UserPatch,
# #     db: Session = Depends(get_db)
# # ):

# #     existing_user = db.query(User).filter(User.id == user_id).first()

# #     if existing_user is None:
# #         raise HTTPException(
# #             status_code=404,
# #             detail="User not found"
# #         )


# #     update_data = user.model_dump(exclude_unset=True)

# #     if user.name is not None:
# #         existing_user.name = user.name

# #     if user.email is not None:
# #         existing_user.email = user.email

# #     if user.age is not None:
# #         existing_user.age = user.age

# #     db.commit()
# #     db.refresh(existing_user)

# #     return existing_user

# ##patch api null value 

# @app.patch("/users/{user_id}")
# def patch_user(
#     user_id: int,
#     user: UserPatch,
#     db: Session = Depends(get_db)
# ):
#     existing_user = db.query(User).filter(User.id == user_id).first()

#     if existing_user is None:
#         raise HTTPException(
#             status_code=404,
#             detail="User not found"
#         )

#     update_data = user.model_dump(exclude_unset=True)

#     for key, value in update_data.items():
#         setattr(existing_user, key, value)

#     db.commit()
#     db.refresh(existing_user)

#     return existing_user


# ## delete api

# @app.delete("/users/{user_id}")
# def delete_user(
#     user_id: int,
#     db: Session = Depends(get_db)
# ):
#     # Find user
#     existing_user = db.query(User).filter(User.id == user_id).first()

#     # If user doesn't exist
#     if existing_user is None:
#         raise HTTPException(
#             status_code=404,
#             detail="User not found"
#         )

#     # Delete user
#     db.delete(existing_user)

#     # Save changes to PostgreSQL
#     db.commit()

#     return {
#         "message": "User deleted successfully"
#     }
#     ## postgresql work end here


##mongodb database start


## JWT authentication start



from fastapi import FastAPI, HTTPException, Depends, Header
from bson import ObjectId
from datetime import datetime, timedelta, timezone
from jose import JWTError, jwt
from fastapi import Request     ##for middleware working, to log the request and response in the console


from database import users_collection
from schemas import UserCreate, UserUpdate, UserPatch
from fastapi import Path
from fastapi import Query




#password hashing
from password import hash_password, verify_password
#password hashing

##cors implememtation start
from fastapi.middleware.cors import CORSMiddleware
##cors implementation end

app = FastAPI()

##cors implememtation start
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
##cors implementation end

## JWT authentication end

#### middleware for logging requests and responses


@app.middleware("http")
async def log_requests(request: Request, call_next):
    print("Request URL:", request.url)

    response = await call_next(request)

    print("Response status:", response.status_code)

    return response
## middleware for logging requests and responses    






# from fastapi import FastAPI, HTTPException, Depends
# from bson import ObjectId
# from jose import jwt



# from database import users_collection
# from schemas import UserCreate, UserUpdate, UserPatch
# from fastapi import Path
# from fastapi import Query

# app = FastAPI()

# # Helper function
# def serialize_user(user):
#     return {
#         "id": str(user["_id"]),
#         "name": user["name"],
#         "email": user["email"],
#         "age": user.get("age")
#     }

# ##dependency inject start

# def new_dept():
#     return{
#     #   'message':'hellow_user'
#       'hello_user'
#     }

# @app.get("/")
# def new_func (newmsg = Depends(new_dept)
# ):
#     return newmsg

# ##dependency inject end


# def get_message():
#     return "Hello FastAPI"

# @app.get("/")
# def home(message: str = Depends(get_message)):
#     return {"message": message}










## dependency injection

@app.get("/")
def home():
    return {"message": "FastAPI is runningg"}


# 1. GET - Get all users

# @app.get("/users")
# def get_users():
#     users = users_collection.find()

#     return [serialize_user(user) for user in users]

########################################## i commented this get user point bcz to test the query and path params , with by using this code as well but some modification, but this code is  working fine for previous task

# # 2. GET - Get user by ID
# @app.get("/users/{user_id}")
# def get_user(user_id: str):
#     if not ObjectId.is_valid(user_id):
#         raise HTTPException(status_code=400, detail="Invalid user ID")

#     user = users_collection.find_one({
#         "_id": ObjectId(user_id)
#     })

#     if not user:
#         raise HTTPException(status_code=404, detail="User not found")

#     return serialize_user(user)


# 3. POST - Create user
# @app.post("/users", status_code=201)
# def create_user(user: UserCreate):
#     existing_user = users_collection.find_one({
#         "email": user.email
#     })

#     if existing_user:
#         raise HTTPException(
#             status_code=400,
#             detail="Email already exists"
#         )

#     user_data = user.model_dump()

#     result = users_collection.insert_one(user_data)

#     created_user = users_collection.find_one({
#         "_id": result.inserted_id
#     })

#     return serialize_user(created_user)




##password hashing code with create user start


# 3. POST - Create user
@app.post("/users", status_code=201)
def create_user(user: UserCreate):
    existing_user = users_collection.find_one({
        "email": user.email
    })

    if existing_user:
        raise HTTPException(
            status_code=400,
            detail="Email already exists"
        )

    user_data = user.model_dump(mode="json")

    user_data["password_hash"] = hash_password(
        user_data.pop("password")
    )

    result = users_collection.insert_one(user_data)

    created_user = users_collection.find_one({
        "_id": result.inserted_id
    })

    return serialize_user(created_user)
##password hashing with cretae user code ends





# 4. PUT - Full update
@app.put("/users/{user_id}")
def update_user(user_id: str, user: UserUpdate):
    if not ObjectId.is_valid(user_id):
        raise HTTPException(status_code=400, detail="Invalid user ID")

    result = users_collection.replace_one(
        {"_id": ObjectId(user_id)},
        user.model_dump()
    )

    if result.matched_count == 0:
        raise HTTPException(status_code=404, detail="User not found")

    updated_user = users_collection.find_one({
        "_id": ObjectId(user_id)
    })

    return serialize_user(updated_user)


# 5. PATCH - Partial update
@app.patch("/users/{user_id}")
def patch_user(user_id: str, user: UserPatch):
    if not ObjectId.is_valid(user_id):
        raise HTTPException(status_code=400, detail="Invalid user ID")

    update_data = user.model_dump(exclude_unset=True)

    if not update_data:
        raise HTTPException(
            status_code=400,
            detail="No fields provided for update"
        )

    result = users_collection.update_one(
        {"_id": ObjectId(user_id)},
        {"$set": update_data}
    )

    if result.matched_count == 0:
        raise HTTPException(status_code=404, detail="User not found")

    updated_user = users_collection.find_one({
        "_id": ObjectId(user_id)
    })

    return serialize_user(updated_user)


# 6. DELETE - Delete user
@app.delete("/users/{user_id}")
def delete_user(user_id: str):
    if not ObjectId.is_valid(user_id):
        raise HTTPException(status_code=400, detail="Invalid user ID")

    result = users_collection.delete_one({
        "_id": ObjectId(user_id)
    })

    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="User not found")

    return {
        "message": "User deleted successfully"
    }
##mongodb end



##path parameters code

# ## path parameter in api with int type
# @app.get("/users/{user_id}")
# def get_user(user_id: int):
#     return {
#         "user_id": user_id
#     }

# @app.get("/users")
# def new_func(
#     age:int=Query(...,gt=0)  ## query validation
# ):
#  return{
#     age:age
# }

# @app.get("/users/{user_id}")
# def neww_funcc(
#     user_id:int= Path(...,gt=0)  ##PATH validation
# ):
#     return{
#         user_id:user_id
#     }

##query and path parameters workign with some changes in user end point to work this query and path param, 
# bcz simple path and query were not working bcz of same end points above, 
# so i make change sin this endpoint and cmmnted the above mongodb users end point

# @app.get("/users")
# def get_users(
#     age: int | None = Query(None, gt=0)
# ):
#     if age is not None:
#         users = users_collection.find({"age": age})
#     else:
#         users = users_collection.find()

#     return [serialize_user(user) for user in users]


## pagination with mongodb



# @app.get("/users")
# def get_users(
#     page: int = Query(1, ge=1),
#     limit: int = Query(10, ge=1, le=100)
# ):
#     # Calculate how many documents to skip
#     skip = (page - 1) * limit

#     # Fetch paginated users
#     users = (
#         users_collection
#         .find()
#         .sort("_id", 1)
#         .skip(skip)
#         .limit(limit)
#     )

#     return [serialize_user(user) for user in users]
##pagination


##search/filter with pagination
@app.get("/users")
def get_users(
    name: str | None = None,
    age: int | None = None,
    page: int = 1,
    limit: int = 30
):
    query = {}

    if name is not None:
        query["name"] = name

    if age is not None:
        query["age"] = age

    skip = (page - 1) * limit

    users = (
        users_collection
        .find(query)
        .skip(skip)
        .limit(limit)
    )

    return [serialize_user(user) for user in users]
## search/filter with pagination


@app.get("/users/{user_id}")
def get_user(user_id: str):
    if not ObjectId.is_valid(user_id):
        raise HTTPException(
            status_code=400,
            detail="Invalid user ID"
        )

    user = users_collection.find_one({
        "_id": ObjectId(user_id)
    })

    if not user:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    return serialize_user(user)

# ## path parameter in api with str type
# @app.get("/users/{name}")
# def get_user(name: str):
#     return {
#         "name": name
#     }

# @app.get('/users/{user_id}')          ##  {} isme jo value dalenge vhi same value function mein same hogi parameter ke andar
#                                       ## The name inside {} should match the function parameter.
# def getuser_info(
#     user_id:int):                        ##   or fr yhi data validate krne ke liye type btayenge uska int hai ya str jo bhi ho

#     return{
#         'user_id': user_id
#     }


# ##multiple path parameters

# @app.get('/users/{user_id_data}/{user_name}')   # 1 url mein user ke 2 parameters same user mein


# ## user parameter and post parameter
# @app.get('/users/{users_id_data}/posts/{posts_id_data}')  ## 1 url mein user ka alg or post ka alag parameter
# def get_user_infoo(users_id_data:int,posts_id_data:int):
#     return{
#      'users_id_data':users_id_data,
#      'posts_id_dataaa':posts_id_data

#     }


##query parameters for learning/practise
# @app.get("/users/{user_id}/post/{post_id}")
# def get_user(user_id:int,post_id:int)
#     return{
#         'user_id':user_id
#         'post_id':post_id
#     }

# @app.get("/users")
# def get_user(age:int)
#     return{
# 'age':int
#     }    


### Authentication
## JWT TOEKN



# from fastapi import FastAPI, HTTPException, Depends
# from bson import ObjectId
# from datetime import datetime, timedelta, timezone
# from jose import JWTError, jwt



# from database import users_collection
# from schemas import UserCreate, UserUpdate, UserPatch
# from fastapi import Path
# from fastapi import Query

# app = FastAPI()

# Demo settings. In a real app, load the secret from an environment variable.
SECRET_KEY = "dkmsaldkawwejnqweqwkepoqwe"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60
REFRESH_TOKEN_EXPIRE_DAYS = 7

##access token
def create_token(data: dict) -> str:
    payload = data.copy()
    expires_at = datetime.now(timezone.utc) + timedelta(
        minutes=ACCESS_TOKEN_EXPIRE_MINUTES
    )
    payload["exp"] = expires_at

    return jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)
##access token

##refresh token
def create_refresh_token(data: dict) -> str:
    payload = data.copy()
    expires_at = datetime.now(timezone.utc) + timedelta(
        days=REFRESH_TOKEN_EXPIRE_DAYS
        # expires_at = datetime.now(timezone.utc) + timedelta(days=7)
    )
    payload["exp"] = expires_at
    return jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)
##refresh token

##login endpoint mein access or refresh token call kro

@app.post("/login")
def login(username: str, password: str):
    if username != "admin" or password != "1234":
        raise HTTPException(status_code=401, detail="Invalid username or password")

    access_token = create_token({"sub": username})
    refresh_token = create_refresh_token({"sub": username})

    return {
        "access_token": access_token,
        "refresh_token": refresh_token,
        "token_type": "bearer"
    }
##login endpoint mein access or refresh token call kro



##refresh token endpoint

@app.post("/refresh")
def refresh(refresh_token: str):
    try:
        payload = jwt.decode(refresh_token, SECRET_KEY, algorithms=[ALGORITHM])
        username = payload.get("sub")
        if not username:
            raise HTTPException(status_code=401, detail="Invalid refresh token")

        new_access_token = create_token({"sub": username})
        return {"access_token": new_access_token, "token_type": "bearer"}

    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid or expired refresh token")
   ##refresh token endpoint




##login end point with only access token
# @app.post("/login")
# def login(username: str, password: str):
#     # Demo-only credentials; a real app should verify a stored password hash.
#     if username != "admin" or password != "1234":
#         raise HTTPException(
#             status_code=401,
#             detail="Invalid username or password",
#         )

#     access_token = create_token({"sub": username})
#     return {"access_token": access_token, "token_type": "bearer"}
##login end point with only access token

def verify_token(authorization: str | None = Header(default=None)) -> dict:
    if authorization is None or not authorization.startswith("Bearer "):
        raise HTTPException(status_code=401, detail="Missing bearer token")

    token = authorization.removeprefix("Bearer ").strip()

    try:
        payload = jwt.decode(
            token,
            SECRET_KEY,
            algorithms=[ALGORITHM],
        )
        username = payload.get("sub")
        if not username:
            raise HTTPException(status_code=401, detail="Invalid token")

        return {"username": username}

    except JWTError:
        raise HTTPException(
            status_code=401,
            detail="Invalid or expired token",
        )


@app.get("/secure")
def secure_data(user: dict = Depends(verify_token)):
    return {
        "message": "Secure data accessed",
        "username": user["username"],
    }

## Authentication
## JWT token