import random
from flask import Flask

facts_list = ["La mayoría de las personas que sufren adicción tecnológica experimentan un fuerte estrés cuando se encuentran fuera del área de cobertura de la red o no pueden utilizar sus dispositivos","El estudio de la dependencia tecnológica es una de las áreas más relevantes de la investigación científica moderna"]

app = Flask(__name__)

@app.route("/")
def hello_world():
    return f'<h1>Datos_aleatorios </h1><a href="/random_fact">¡Ver un dato aleatorio!</a>'

@app.route("/random_fact")
def hello_world():
    return f'<p>{random.choice(facts_list)}</p>'

@app.route("/random_fact")
    <a href="/random_fact">¡Ver un dato aleatorio!</a>

@app.route("/RUTA")
def NOMBRE_DE_LA_FUNCION():

app.run(debug=True)
