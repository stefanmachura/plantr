FROM python:3.9-slim

WORKDIR /opt/app

RUN apt-get update && apt-get upgrade -y

RUN apt-get install netcat gcc libpq-dev python-dev -y

RUN pip install --upgrade pip
COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

COPY ./entrypoint.sh .

ENTRYPOINT ["/opt/app/entrypoint.sh"]