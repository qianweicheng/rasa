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
pip install -U -e.
```

###
3) Train model
SKIP this step unless you would like to retrain a model
````
python -m edo_pro.rasasc_jeff -t
````
###
4) Run model
```
python -m edo_pro.rasasc_jeff -r
```

###
5) Get Http Response : 
Follow this format: curl http://localhost:5005/model/answer -d '{"text":" YOUR QUESTION "}'
Examples
````
curl http://localhost:5005/model/answer -d '{"text":"Please delete my account"}'
````
````
curl http://localhost:5005/model/answer -d '{"text":"I've accidentally downloaded and signed up for Edison Assistant instead of Email. How do I cancel my Assistant account?"}'
````
````
curl http://localhost:5005/model/answer -d '{"text":"how do i enable dark mode?"}'
````