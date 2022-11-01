## Set for backend

```BASH
git clone https://github.com/geksogen/Scalable_Streamlit-_Apps.git
cd backend/app
sh prepare_models.sh
sudo apt-get update
sudo apt install python3-pip
pip3 install -r ../requirements.txt
python3 ./main.py
```

## Set for frontend
```BASH
git clone https://github.com/geksogen/Scalable_Streamlit-_Apps.git
cd frontend/app
pip3 install -r ../requirements.txt
pip3 install --upgrade jinja2
python3 -m streamlit run main.py
```

https://python.astrotech.io/fastapi/fastapi/http-files.html



