FROM python:3.6.12-alpine

WORKDIR /code

COPY requirements.txt /code

RUN pip install --upgrade pip

RUN pip install -r requirements.txt --no-cache-dir

COPY . /code

ENTRYPOINT ["./gunicorn.sh"]