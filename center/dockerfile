FROM python:3.8-slim-buster

RUN apt-get update \
    && apt-get install -y gcc python3-dev musl-dev  libffi-dev netcat vim\
    && mkdir /center

WORKDIR /center
COPY ./requirements.txt /center
RUN pip install -r requirements.txt

EXPOSE 8080
CMD ["python", "manage.py", "runserver", "0.0.0.0:8080"]