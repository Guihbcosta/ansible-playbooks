from flask import Flask
from redis import Redis, RedisError
import os

redis = Redis(host="redis", port=6379)

app = Flask(__name__)

@app.route("/")
def ola_mundo():
    try:
        visits = redis.incr("counter")
    except RedisError:
        visits = "<i>Sem conexao com o Redis, contador desabilitado<i>"
    
    html = "<h3>Ola {name}!<h3>" \
           "<b>Visitas:</b> {visits}"
    
    return html.format(
        name=os.getenv("NAME", "Visitante"),
        visits=visits
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)