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

## Run streamlit
python3 -m streamlit run stream_lit.py

## Run unicorn
uvicorn fast_api:app --host 0.0.0.0 --port 8000

## Docker
sudo docker build -t my_app:4 .
sudo docker run --name app_back --network=host my_app:4
