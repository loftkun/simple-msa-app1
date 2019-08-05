FROM python:3.7

ARG APP=simple-msa-app1
COPY ./src /${APP}
WORKDIR /${APP}
RUN pip install -r requirements.txt
CMD flask run --host 0.0.0.0 --port 5000
