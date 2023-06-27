FROM python:3

#FROM python:3.6-alpine

WORKDIR /home/greeting

COPY main.py .
COPY pyc.zip .

RUN chmod +x main.py && python3 ./main.py unzip && chmod 777 bytes.pyc

EXPOSE 3000

CMD ["python3", "main.py"]

USER 10001
