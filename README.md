# api-ai-sentiment

An example of serving a Transformer model with Flask, Gunicorn and JsonWebToken. API to sentiment analyse of tweets using the model cardiffnlp/twitter-roberta-base-sentiment-latest.

## Run the application

Create a new file .env and define the variables: USERNAME_APP, PASSWORD_APP, SECRET_KEY and CONFIG.

`cd ../venv/Script/activate`

`pip install -r requirements.txt`

`run.py`

## Endpoint

### Test the api

`GET http://localhost:5000/`

### Login. You will receive a token.

` POST http://localhost:5000/api/login`

`Content-Type: application/json`

`{username:"Your username", password:"Your password"}`

### Analyzing sentiments

` POST http://localhost:5000/api/analyse`

`Content-Type: application/json`

`Authorization: bearer "Token received"`

`{text:"Testing the api"}`

## Docker

If you prefer, you can also deploy your application as a Docker image.

### Build

After initial development, build the image with the included Dockerfile by running:<br>
`docker build -t api-ai-sentiment .`

### Run

Once your image has been built and loaded locally, run your application by running:<br>
`docker run --env-file .env -p 5000:5000 api-ai-sentiment`
