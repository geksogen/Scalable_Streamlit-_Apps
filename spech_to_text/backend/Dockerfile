# temp stage
FROM nvidia/cuda:11.8.0-base-ubuntu22.04
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Add Python ppa
RUN apt-get update && apt-get install -y software-properties-common
RUN DEBIAN_FRONTEND=noninteractive TZ=Etc/UTC apt-get -y install tzdata
RUN add-apt-repository ppa:deadsnakes/ppa
# Install essential Ubuntu packages
# and upgrade pip
RUN apt-get install -y \
    curl \
    python3.9 &&\
    ln -s /usr/bin/python3.9 /usr/local/bin/python &&\
    ln -s /usr/bin/python3.9 /usr/local/bin/python3 &&\
    curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py &&\
    python3 get-pip.py &&\
    rm get-pip.py &&\
    # best practice to keep the Docker image lean
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*
RUN python -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

# final stag
FROM nnvidia/cuda:11.8.0-base-ubuntu22.04
COPY --from=builder /opt/venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

WORKDIR /code
COPY ./requirements.txt /code/requirements.txt
COPY ./app /code/app
RUN mkdir -p /tmp/save
#RUN sudo apt install ffmpeg
RUN pip install -r /code/requirements.txt

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8081"]
