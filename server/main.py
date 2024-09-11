from fastapi import FastAPI
import os

# Initialize FastAPI app
app = FastAPI()

# Endpoint to respond with "Hello World"
@app.get("/")
async def root():
    return {"message": "Hello World"}

# Start the FastAPI server using uvicorn
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
