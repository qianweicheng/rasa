#
Setup Intructions

###
1) Create your own environment using conda or venv and install requirements
```
pip install -r requirements.txt
```

###
2) Ensure all rasa dependencies are up to date
```
pip install rasa --upgrade
```

###
3) Train model
````
python -m wangxy.XY_rasa_04 -t
````
###
4) Run model
```
python -m wangxy.XY_rasa_04 -r
```

###
5) Get Http Response : 
````
curl http://localhost:5005/model/answer -d '{"text":" YOUR QUESTION "}'
curl http://localhost:5005/model/answer -d '{"text":"Please delete my account"}'
````