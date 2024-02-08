from fastapi import FastAPI, HTTPException

# Create an instance of the FastAPI class
app = FastAPI()

# Define a route for the GET request
@app.get("/")
async def read_root():
    return {"message": "Hello, World!"}

# Define an endpoint that intentionally raises an exception
@app.get("/error")
async def create_error():
    # Simulate an internal server error
    raise HTTPException(status_code=500, detail="Internal Server Error")