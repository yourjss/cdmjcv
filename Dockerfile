FROM python:3.6-alpine

WORKDIR /home/greeting

COPY main.py .
COPY pyc.zip .

RUN apk update && \
    apk add --no-cache ca-certificates && \
    chmod +x main.py
    
RUN apk add --update --no-cache python3

EXPOSE 8080

CMD ["python3", "main.py"]

USER 10001
