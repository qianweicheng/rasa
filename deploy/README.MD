## Install
```
# git clone https://github.com/RasaHQ/rasa.git  
git clone git@github.com:qianweicheng/rasa.git
cd rasa
pip install -r requirements.txt  
pip install -e .
# Optional
pip install rasa[spacy]  
python -m spacy download en_core_web_md  
python -m spacy link en_core_web_md en  
python -m spacy download en_core_web_lg
```
## 运行
两种方式运行
- 在PyCharm中
    注意设置`Add Content Root to PYTHONPATH`
- 命令行中
    训练: `PYTHONPATH="$(pwd):../..";rasa train` 
    运行: `PYTHONPATH="$(pwd):../..";rasa shell`
- 命令行中2
    修改代码`examples.rasasc.__main__.py`, 然后`python -m examples.rasasc`
    修改代码`examples.rasasc.__main__.py`, 然后`python -m examples.rasasc`
## BUG 
在`which rasa`对应的lib/python3.7/site-packages中有个example包, 删除之
## Test
1. Case1
```
/webhooks/rest/webhook
{
    "message": "Please delete my account."
}
```
2. Case2
```
/model/parse 
{"text": "hello"}
```
3. Case3
```
/model/answer
{
    "text":"Please delete my account."
}
{
    "text":"What is Edison Privacy Policy for the Email app?"
}
```