FROM python:3.6.12-alpine

WORKDIR /code

COPY requirements.txt /code

ENV USERNAME_APP API-TWITTER-SENTIMENT
ENV PASSWORD_APP bxacxd0xcfx18y!xb3!xd6c!xea&!xb6!x01=j!x04!xa7j!xfa!xc9!xe4_G!xa5!xb0
ENV SECRET_KEY aplicacion*que*analiza*el*sentimiento*de*una*frase*ViPo*DeSaRrolLadORR-33!
ENV CONFIG DEV

RUN pip install --upgrade pip

RUN pip install -r requirements.txt --no-cache-dir

COPY . /code

ENTRYPOINT ["./gunicorn.sh"]