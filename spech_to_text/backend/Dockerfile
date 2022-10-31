# temp stage
FROM debian:8
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update
RUN apt install python3
RUN python -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

# final stag
FROM debian:8
COPY --from=builder /opt/venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

WORKDIR /code
COPY ./requirements.txt /code/requirements.txt
COPY ./app /code/app
RUN mkdir -p /tmp/save
RUN wget "https://github.com/pytorch/TensorRT/archive/refs/tags/v1.1.1.zip"
RUN pip install v1.1.1.zip
RUN rm -rf v1.1.1.zip
#RUN sudo apt install ffmpeg
RUN pip install -r /code/requirements.txt

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8081"]
