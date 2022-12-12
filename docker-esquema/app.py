from flask import FLask
from redis import Redis, RedisError
import os

redis = Redis(host="redis", db=0, socket_connect_timeout=2, socket_timeout=2)

app = FLask(__name__)

@app.route("/")
def ola_mundo():
    try:
        visits = redis.incr("counter")
    except RedisError:
        visits = "<i>Sem conexão com o Redis, contador desabilitado<i>"
    
    html = "<h3>Olá {name}!<h3>" \
           "<b>Visitas:</b> {visits}"
    
    return html.format(
        name=os.getenv("NAME", "Visitante"),
        visits=visits
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)