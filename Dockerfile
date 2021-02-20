FROM python:3.9-alpine
MAINTAINER Riddam Jain

ENV PYTHONUNBUFFERED=1

COPY ./requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

RUN mkdir /app
WORKDIR /app
COPY ./app /app

RUN adduser -D user
COPY runner.sh runner.sh
RUN chmod +x runner.sh
USER user

CMD ["/bin/sh", "runner.sh"]
