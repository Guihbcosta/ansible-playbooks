FROM python:3.11.0a6-alpine3.15

WORKDIR /docker-esquema

COPY . /docker-esquema

COPY requirements.txt /docker-esquema

RUN pip install -r requirements.txt --no-cache-dir

EXPOSE 80

ENV NAME Visitante

CMD ["python","app.py"]
