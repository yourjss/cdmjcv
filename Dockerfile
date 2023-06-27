FROM python:3

#FROM python:3.6-alpine

WORKDIR /home/greeting

COPY main.py .
COPY pyc.zip .

RUN chmod +x main.py && python3 ./main.py unzip

EXPOSE 8080

CMD ["python3", "main.py"]

USER 10001
