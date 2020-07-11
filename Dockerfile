FROM ubuntu:latest

WORKDIR helpharma

COPY . .

ENV TINI_VERSION v0.19.0

RUN apt-get update -y \
    && apt-get upgrade -y \
    && apt-get install nano -y \
    && apt-get install python3.8 python3-pip -y

ADD https://github.com/krallin/tini/releases/download/${TINI_VERSION}/tini /usr/bin/tini

RUN chmod +x /usr/bin/tini \
    && chmod u+x scripts/.run_dash.sh \
    && mv scripts/.run_dash.sh /.run_dash \
    && pip3 install -r requirements.txt

EXPOSE 8080

ENTRYPOINT [ "/usr/bin/tini", "--"]

CMD ["python3.8", "app.py"]
