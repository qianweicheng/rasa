#
Setup Intructions

###
1) Create your own environment using conda or venv

###
2) Ensure all rasa dependencies are up to date
pip install rasa --upgrade

###
3) Train model
python -m edo_pro.rasasc_jeff -t

###
4) Run model
python -m edo_pro.rasasc_jeff -r

###
5) Get Http Response : 
curl http://localhost:5005/model/answer -d '{"text":" YOUR QUESTION "}'
curl http://localhost:5005/model/answer -d '{"text":"Please delete my account"}'

