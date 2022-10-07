FROM python:3.10-slim-bullseye

WORKDIR /code

COPY requirements.txt /code

RUN pip install --upgrade pip

RUN pip install -r requirements.txt --no-cache-dir

COPY . /code

CMD ["gunicorn", "--timeout", "600","--workers", "4", "run:app", "--preload", "-b", "0.0.0.0:5000"]