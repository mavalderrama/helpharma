FROM ubuntu:latest

WORKDIR helpharma

COPY . .

RUN apt-get update -y \
    && apt-get upgrade -y \
    && apt-get install python3.8 python3-pip -y

RUN chmod +x /usr/bin/tini \
    && pip3 install -r requirements.txt

CMD python3.8 app.py $PORT
