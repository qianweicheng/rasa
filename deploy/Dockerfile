# use this prebuild base image to accelerate the deploy speed.
# the cost is the image size is >1G
FROM hub.edisonpark.net/edisonchat/rasa:tools

EXPOSE 5005

#ENTRYPOINT ["rasa"]
#CMD ["--help"]

COPY ./edo_pro ./edo_pro
ENTRYPOINT ["python"]
CMD ["-m", "edo_pro.rasasc_jeff", "-r"]
