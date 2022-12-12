FROM python:3.11.0a6-alpine3.15

WORKDIR /docker-esquema

COPY . /docker-esquema

RUN pip install --trusted-host pypi.python.org -r requirements.txt

EXPOSE 80

ENV NAME Visitante

CMD ["python","app.py"]
