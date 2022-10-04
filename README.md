# api-ai-sentiment
An example of serving a Transformer model with Flask and Gunicorn. API to sentiment analyse of tweets using the model cardiffnlp/twitter-roberta-base-sentiment-latest.

## Docker
If you prefer, you can also deploy your application as a Docker image.

### Build
After initial development, build the image with the included Dockerfile by running:<br>
  `docker build -t api-ai-sentiment .`
  
  
### Run
Once your image has been built and loaded locally, run your application by running:<br>
 `docker run --env-file .env -p 5000:5000  hta-sentiment`
