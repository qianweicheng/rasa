# use this prebuild base image to accelerate the deploy speed.
# the cost is the image size is >1G
FROM hub.edisonpark.net/edisonchat/rasa:tools

EXPOSE 5005

COPY ./edo_pro ./edo_pro
ADD https://edison-static.s3-us-west-2.amazonaws.com/rasa-model/20200526-181834.tar.gz ./edo_pro/rasasc_jeff/models/

ENTRYPOINT ["python"]
CMD ["-m", "edo_pro.rasasc_jeff", "-r"]

# run via docker 
# docker run -d \
# --name rasa \
# -v `pwd`/edo_pro:/app/edo_pro \
# -p 5006:5005 \
# --entrypoint python \
# hub.edisonpark.net/edisonchat/rasa:tools \
# -m edo_pro.rasasc_jeff -r