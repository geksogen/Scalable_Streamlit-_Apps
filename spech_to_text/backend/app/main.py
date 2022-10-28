import uuid
import uvicorn
from fastapi import File
from fastapi import FastAPI
from fastapi import UploadFile
import aiofiles
import asyncio
import json
from vosk import Model, KaldiRecognizer, SetLogLevel
from pydub import AudioSegment
import json
import os

app = FastAPI()


@app.get("/")
def read_root():
    return {"message": "Welcome from the API"}


@app.post("/upload")
async def post_endpoint(file: bytes = File(...)):

    #Save Upload file to disk
    async with aiofiles.open('./save/soung.mp3', 'wb') as out_file:
        await out_file.write(file)  # async write

        startMin = 0
        startSec = 0
        endMin = 0
        endSec = 60

        # Time to miliseconds
        startTime = startMin * 60 * 1000 + startSec * 1000
        endTime = endMin * 60 * 1000 + endSec * 1000

        # Opening file and extracting segment
        song = AudioSegment.from_mp3('./save/soung.mp3')
        extract = song[startTime:endTime]

        # Saving
        extract.export('./save/extract.mp3', format="mp3")

    #return {"name": content}


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8081)
