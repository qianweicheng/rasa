
# Install
```
git clone https://github.com/RasaHQ/rasa.git  
cd rasa
virtualenv -p python3 venv
pip install --upgrade pip    
pip install -r requirements.txt  
pip install -e .  

pip install rasa[spacy]  
python -m spacy download en_core_web_md  
python -m spacy link en_core_web_md en  
python -m spacy download en_core_web_lg
```
## Run
- 在根目录下
    `python -m examples.rasasc`
- 在examples/rasasc目录下  
    - 使用`pip install -e . `，把rasa安装到site-packages里面了rasa.egg-link(其实就是一个快捷方式)，所以可以直接  
    `rasa train` or `rasa shell`
    - 没有安装rasa的话，则需要
    ```
    PYTHONPATH="`pwd`:../..";rasa train
    PYTHONPATH="`pwd`:../..";rasa shell
    ```