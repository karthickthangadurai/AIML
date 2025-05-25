from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World",'name':'karthick'}

@app.get("/hello")
def say_hello():
    return {"greeting": "Hi there!"}

@app.get("/toys")
def show_toys():
    return {"toy": "car"}

@app.post("/toys")
def add_toy(toy: dict):
    print(toy)
    return {"message": "Added new toy!", "toy": toy}

@app.put("/toys/1")
def update_toy(toy_id: int, new_toy: dict):
    return {"message": f"Updated toy {toy_id}", "new_toy": new_toy}


from pydantic import BaseModel

# Define what the JSON should look like
class UserCreate(BaseModel):
    name: str
    email: str
    age: int

@app.post("/users")
def create_user(user: UserCreate):
    return {
        "message": "User created!",
        "user_name": user.name,
        "user_email": user.email,
        "user_age": user.age
    }

from fastapi import FastAPI, BackgroundTasks
import time

# This is a slow function (like sending an email or processing data)
def send_email(email: str):
    print(f"⏳ Starting to send email to {email}...")
    time.sleep(5)  # Simulates a slow task
    print(f"✅ Finished sending email to {email}!")

# FastAPI route

@app.post("/subscribe")
async def subscribe(email: str, background_tasks: BackgroundTasks):
    print("🔴 Before adding background task")
    background_tasks.add_task(send_email, email)
    print("🟢 After adding background task")
    return {"message": f"Thanks! We'll send updates to {email} soon."}