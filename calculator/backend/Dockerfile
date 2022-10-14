FROM python:3.8-slim-buster

WORKDIR /code

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY ./fast_api.py /code/

CMD [ "uvicorn", "fast_api:app", "--host=0.0.0.0", "--port=8000"]