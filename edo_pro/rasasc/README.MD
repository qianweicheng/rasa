
sudo pip install -r requirements.txt --user  
sudo pip install -e . --user  

pip install --upgrade pip  

git clone https://github.com/RasaHQ/rasa.git  
cd rasa  
pip install -r requirements.txt  
pip install -e .  

pip install rasa[spacy]  
python -m spacy download en_core_web_md  
python -m spacy link en_core_web_md en  

python -m spacy download en_core_web_lg


PYTHONPATH="`pwd`:../..";rasa train
PYTHONPATH="`pwd`:../..";rasa shell

create file 
execute
copy file
