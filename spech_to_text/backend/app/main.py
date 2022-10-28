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
async def post_endpoint(file: bytes | None = File(None)):
    #bytes_data = file
    #f = open("./save/soung.mp3", "wb")
    #f.write(bytes_data)
    #f.close()
    if not file:
        return {'message': 'No file sent'}
    else:
        async with aiofiles.open('./save/soung.mp3', mode = 'wb', ) as out_file:
            content = await file.read()  # async rea
            await out_file.write(file)  # async write
            #return {'name': , 'bytes': len(file)}


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8081)
