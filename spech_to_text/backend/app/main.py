import uuid
import uvicorn
from fastapi import File
from fastapi import FastAPI
from fastapi import UploadFile
import aiofiles
import asyncio
import json
import hashlib

app = FastAPI()


@app.get("/")
def read_root():
    return {"message": "Welcome from the API"}


@app.post("/upload")
async def post_endpoint(file: UploadFile=File(...)):
    async with aiofiles.open('./save/soung.mp3', mode = 'wb', ) as out_file:
        buffer_size = 2 ** 10 * 8
        file_hash = hashlib.sha256()
        content = await file.read(buffer_size)  # async rea
        await out_file.write(content)  # async write
    return {"name": content}


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8081)
