# Deploy
## Steps
- pull code
- prepare third libraries
- train
- run
## Install
```
# git clone https://github.com/RasaHQ/rasa.git  
git clone git@github.com:qianweicheng/rasa.git
cd rasa
virtualenv -p python3 venv
pip install -r requirements.txt
# install rasa as ediable，把rasa安装到site-packages里面作为rasa.egg-link(其实就是一个快捷方式)
pip install -e .
# Optional
pip install rasa[spacy]  
python -m spacy download en_core_web_md  
python -m spacy link en_core_web_md en  
python -m spacy download en_core_web_lg
```
## 运行
- 在PyCharm中
    由于PyCharm默认会`Add Content Root to PYTHONPATH`，所以直接运行就OK
- 命令行中(如果当前目录在examples/rasasc)
    - 使用了`pip install -e . `，所以可以直接运行`rasa train; rasa shell`
    - 否则需要添加rasa到PYTHONPATH
    ```
    PYTHONPATH="$PYTHONPATH:../..";rasa train
    PYTHONPATH="$PYTHONPATH:../..";rasa shell
    ```
- 命令行中(在根目录下)
    `python -m edo_pro.rasasc -h` (因为在edo_pro.rasasc有__main__.py文件)
## BUG 
在`which rasa`对应的lib/python3.7/site-packages中有个example包, 删除之
## APIS
Backend: http://cp.stag.easilydo.cc/api/rasa/
Frontend: https://admin.stag.easilydo.cc:8091
## Deploy 
We should change the Dockerfile ENTRYPOINT if we want to run another model.
## Test
- Case1
```
/webhooks/rest/webhook {"message": "Please delete my account."}
```
- Case2
```
/model/parse {"text": "hello"}
```
- Case3
```
/model/answer {"text":"Please delete my account."} 
/model/answer {"text":"What is Edison Privacy Policy for the Email app?"}
```
## Deploy
1. Upload the model to S3
2. Update Dockerfile
3. Run Jenkins