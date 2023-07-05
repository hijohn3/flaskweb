from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello, Flask"

@app.get('/hello/<name>', endpoint="hello-point")
def hello(name):
    return f"Hello, {name}!"

@app.route("/name/<name>")
def show_name(name):
    #retrun variable to template_engine
    return render_template("index.html", name=name)