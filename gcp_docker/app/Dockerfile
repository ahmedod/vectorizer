FROM python:3.7.1-stretch

LABEL MAINTAINER="oued ahm <ouederni2015@gmail.com>"

ENV GROUP_ID=1000 \
    USER_ID=1000

WORKDIR /var/bbb/

ADD . /var/bbb/
RUN pip install -r requirements.py
RUN pip install gunicorn

#RUN addgroup -g $GROUP_ID www
#RUN adduser -D -u $USER_ID -G www www -s /bin/sh

#USER www

EXPOSE 5000
ENV export GOOGLE_APPLICATION_CREDENTIALS key.json
RUN export GOOGLE_APPLICATION_CREDENTIALS="key.json"
#CMD [ "gunicorn", "-w", "4", "--bind", "0.0.0.0:5000", "wsgi"]
CMD ["python", "manage.py"]
