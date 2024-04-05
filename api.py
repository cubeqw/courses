import hashlib
from fastapi_sqlalchemy import DBSessionMiddleware, db
from fastapi import FastAPI
import uvicorn
from models import UserModel
from models import CourseModel
from schema import User
from email_validator import validate_email

app = FastAPI()
app.add_middleware(DBSessionMiddleware, db_url='postgresql://postgres:1234@localhost/pp2')


@app.get("/")
async def read_root():
    return {"Hello": "World"}


@app.post("/register/")
async def create_user(user: User):
    if validate_email(user.email):
        if len(user.password) >= 8:
            # Create a new session
            # Create a new user object using the request data
            hash = hashlib.sha256(user.password.encode()).hexdigest()
            new_user = UserModel(password=hash, email=user.email)
            # Add the user to the session
            db.session.add(new_user)
            # Commit the session to persist the changes
            db.session.commit()
            # Close the session
            db.session.close()
            return {"message": "User created successfully"}
        else:
            return {"error": "Password is short"}
    else:
        return {"error": "Invalid email"}

@app.get("/courses/")
async def get_courses():
    course = db.session.query(CourseModel).all()
    return course

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=5000, log_level="info")
