import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List


# Define the Fruit model
class Fruit(BaseModel):
    name: str

# Define the Fruits model
class Fruits(BaseModel):
    fruits: List[Fruit]

# Initialize the FastAPI app
app = FastAPI()


#settings
# CORS settings
origins = [
    "http://localhost:3000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# In-memory database
memory_db = {"fruits": [{"name": "Cookies"}, {"name": "Cream"}]}

# GET endpoint to fetch fruits
@app.get("/fruits", response_model=Fruits)
def get_fruits():
    return Fruits(fruits=memory_db["fruits"])


# /login 
    # username, email, password, phone_number 
    # check if the users is logged in in the database
    # return that usewr loged 
#/signUp


# POST endpoint to add a fruit
@app.post("/fruits")
def add_fruit(fruit: Fruit):
    memory_db["fruits"].append(fruit.dict())  # Ensure the new fruit is converted to a dictionary
    return fruit


# Run the app
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
