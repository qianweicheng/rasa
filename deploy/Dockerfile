FROM python:3

VOLUME ["/app"]
WORKDIR /app

COPY ./ ./

EXPOSE 5005

ENTRYPOINT ["python -m examples.rasasc"]

CMD ["--help"]
