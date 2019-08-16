# 运行
两种方式运行
- 在PyCharm中
    注意设置`Add Content Root to PYTHONPATH`
- 命令行中
    打开venv: `source venv/bin/active`
    运行: `PYTHONPATH="`pwd`:../..";rasa train`
## BUG 
在`which rasa`对应的lib/python3.7/site-packages中有个example包, 删除之