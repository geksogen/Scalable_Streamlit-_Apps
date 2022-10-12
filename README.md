# Scalable_Streamlit-_Apps

## Поднимаем VM из terraform
Конфигурация VM - дирректория test_to

```BASH
sudo apt-get update
sudo apt install uvicorn
sudo apt install python3-pip

pip3 install -r requirements.txt
pip3 install FastAPI[all]
pip3 install --upgrade jinja2


```

## Создаем Dockerfile

```BASH
# Dockerfile to create a Docker image for the demo-face-gan Streamlit app

# Creates a layer from the python:3.7 Docker image
FROM python:3.7

# Copy all the files from the folders the Dockerfile is to the container root folder
COPY . .

# Install the modules specified in the requirements.txt
RUN pip3 install -r requirements.txt

# The port on which a container listens for connections
EXPOSE 8501

# The command that run the app
CMD streamlit run app.py
```

https://stackoverflow.com/questions/68673221/warning-running-pip-as-the-root-user


## Run streamlit
python3 -m streamlit run stream_lit.py

## Run unicorn
uvicorn fast_api:app --host 0.0.0.0 --port 8000



