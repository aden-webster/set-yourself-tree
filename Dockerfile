FROM python:3 

LABEL MAINTAINER="aden@a-webster.com"
COPY . /app
WORKDIR /app
ADD requirements.txt /app

RUN pip install --no-cache-dir  -r /app/requirements.txt

CMD [ "python", "./tree.py" ]