from fastapi import FastAPI
import os
import asyncio
import sys
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
sys.path.append(os.getenv('PYTHONPATH'))
from bot.bot import client

# Initialize FastAPI app
app = FastAPI()

# Endpoint to respond with "Hello World"
@app.get("/")
async def root():
    return {"message": "Hello World"}

async def start_bot():
    token = os.getenv('TOKEN')
    await client.start(token)

async def start_server():
    import uvicorn
    config = uvicorn.Config("main:app", host="0.0.0.0", port=8000, reload=True)
    server = uvicorn.Server(config)
    await server.serve()

async def main():
    # Run the FastAPI server and Discord bot concurrently
    await asyncio.gather(start_server(), start_bot())

if __name__ == "__main__":
    asyncio.run(main())
