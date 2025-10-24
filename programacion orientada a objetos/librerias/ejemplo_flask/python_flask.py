# DEBES DE INSTALAR FLASK CON: pip install Flask
from flask import Flask

app = Flask(__name__)

@app.route("/")
def inicio():
    return "<h1>Inicio</h1>"

@app.route("/youtube")
def youtube():
    return '<iframe width="560" height="315" src="https://www.youtube.com/embed/B3XM2nZt6RM?si=fI__3yxH_6fqyOdt" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>'

app.run(debug=True)