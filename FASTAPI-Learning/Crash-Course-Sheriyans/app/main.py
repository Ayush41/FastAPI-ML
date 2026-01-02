from fastapi import FastAPI

app = FastAPI()

# Running the server on Localhost :8000

# GET -> Read a resource
@app.get('/')
def root():
    return {"message":"Welcome to Root page"} 
    
    # POST -> Create a new resource
    # PUT -> Update an existing resource
    # PATCH -> Update a specific field of a resource
    # DELETE -> Delete a resource

