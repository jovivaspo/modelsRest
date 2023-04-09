# ModelsRest

It provides a set of endpoints that allow developers to integrate language models into their applications. Using Flask-restx, Gunicorn and JsonWebToken.<br>

- Translate: facebook/nllb-200-distilled-600M
- Extract Keyworks: sentence-transformers/distiluse-base-multilingual-cased-v2
- Paraphrase: tuner007/pegasus_paraphrase
- Summarize: google/pegasus-xsum
- Analyse sentiment: cardiffnlp/twitter-roberta-base-sentiment-latest

## Run the application

Create a new file .env and define the variables: USERNAME_APP, PASSWORD_APP, JWT_SECRET_KEY and CONFIG.

Create an environment

`python3 -m venv venv`

`cd venv/Scripts/activate`

`pip install -r requirements.txt`

`run.py`

## Documentation

You can review the documentation and available endpoints at http://localhost:5000/api/v1/

### Test the api

`GET http://localhost:5000/`

### Login. You will receive a token.

` POST http://localhost:5000/api/v1/login/`

`Content-Type: application/json`

`{username:"Your username", password:"Your password"}`

## Docker

If you prefer, you can also deploy your application as a Docker image.

### Build

After initial development, build the image with the included Dockerfile by running:<br>
`docker build -t modelrest .`

### Run

Once your image has been built and loaded locally, run your application by running:<br>
`docker run --env-file .env -p 5000:5000 modelrest`
