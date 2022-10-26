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
## Docker-compose
```BASH
sudo apt-get install curl
sudo apt-get install gnupg
sudo apt-get install ca-certificates
sudo apt-get install lsb-release

### Download the docker gpg file to Ubuntu
sudo mkdir -p /etc/apt/keyrings
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg

### Add Docker and docker compose support to the Ubuntu's packages list
echo "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/sudo apt-get install docker-ce docker-ce-cli containerd.io docker-compose-pluginsudo apt-get install docker-ce docker-ce-cli containerd.io docker-compose-pluginlinux/ubuntu   $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
sudo apt-get update

### Install docker and docker compose on Ubuntu
sudo apt-get install docker-ce docker-ce-cli containerd.io docker-compose-plugin
```

