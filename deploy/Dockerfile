# use this prebuild base image to accelerate the deploy speed.
# the cost is the image size is >1G
FROM hub.edisonpark.net/edisonchat/rasa:tools

# Because base image has been disable pip install
USER 0
EXPOSE 5005


COPY ./edo_pro ./edo_pro
# COPY ./edo_bert_finetune ./edo_bert_finetune
# COPY ./edo_plugin ./edo_plugin

RUN mkdir -p ./edo_pro/wangxy/XY_rasa_04/models
ADD https://edison-static.s3-us-west-2.amazonaws.com/rasa-model/20200723-133134.tar.gz ./edo_pro/wangxy/XY_rasa_04/models/
# RUN cd ./edo_pro/rasasc_jeff; pip install -r requirements.txt
RUN cd ./edo_pro/wangxy/XY_rasa_04

ENTRYPOINT ["python"]
CMD ["-m", "edo_pro.wangxy.XY_rasa_04", "-r"]