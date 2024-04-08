FROM python:3 

LABEL MAINTAINER="aden@a-webster.com"
COPY . /app
WORKDIR /app
ADD requirements.txt /app
RUN pip install -r /app/requirements.txt

CMD [ "python", "./tree.py" ]