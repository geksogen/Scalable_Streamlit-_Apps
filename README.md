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

https://stackoverflow.com/questions/68673221/warning-running-pip-as-the-root-user
https://fastapi.tiangolo.com/deployment/docker/#build-a-docker-image-for-fastapi

## Run streamlit
python3 -m streamlit run stream_lit.py

## Run unicorn
uvicorn fast_api:app --host 0.0.0.0 --port 8000

## Docker build and run

```BASH
#build
sudo docker build -t my_front:1 .
sudo docker build -t my_back:1 .
#run
sudo docker run --rm -d --name app_front --network=host my_front:1
sudo docker run --rm -d --name app_back --network=host my_back:1
#clear
sudo docker stop $(sudo docker ps -aq)
sudo docker rm $(sudo docker ps -aq)
sudo docker rmi $(sudo docker images -q)
```



