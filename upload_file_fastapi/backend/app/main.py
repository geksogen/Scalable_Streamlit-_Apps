import uuid
import uvicorn
from fastapi import File
from fastapi import FastAPI
from fastapi import UploadFile
import aiofiles
import asyncio
import json


app = FastAPI()


@app.get("/")
def read_root():
    return {"message": "Welcome from the API"}


@app.post("/upload")
async def post_endpoint(file: UploadFile=File(...)):
    async with aiofiles.open('/tmp/save/tmp.txt', 'wb') as out_file:
        content = await file.read()  # async read
        await out_file.write(content)  # async write
    return {"name": content}
#

#if __name__ == "__main__":
#    uvicorn.run("main:app", host="0.0.0.0", port=8081)
