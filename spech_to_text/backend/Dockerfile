# temp stage
FROM python:3.9-slim as builder
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update
RUN python -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

# final stag
FROM python:3.9-slim
COPY --from=builder /opt/venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

WORKDIR /code
COPY ./requirements.txt /code/requirements.txt
COPY ./app /code/app
RUN mkdir -p /tmp/save
#RUN sudo apt install ffmpeg
RUN pip install -r /code/requirements.txt

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8081"]
