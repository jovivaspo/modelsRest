FROM python:3.6-slim

WORKDIR /code

COPY requirements.txt /code

RUN pip install --upgrade pip

RUN pip install -r requirements.txt --no-cache-dir

COPY . /code

CMD ["gunicorn", "run:app", "-b", "0.0.0.0:5000"]