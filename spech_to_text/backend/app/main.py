import uuid
import uvicorn
from fastapi import File
from fastapi import FastAPI
from fastapi import UploadFile
import aiofiles
import asyncio
import json
from pathlib import Path
app = FastAPI()


@app.get("/")
def read_root():
    return {"message": "Welcome from the API"}


@app.post("/upload")
async def post_endpoint(file: bytes = File(...)):
    #bytes_data = file
    #f = open("./save/soung.mp3", "wb")
    #f.write(bytes_data)
    #f.close()

    #path = Path('/save') / file.filename
    #size = path.write_bytes(await file.read())
    #return {'name': size}

    async with aiofiles.open('./save/soung.mp3', 'wb') as out_file:
        #content = await file.read()  # async read
        await out_file.write(file)  # async write
    #return {"name": content}


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8081)
