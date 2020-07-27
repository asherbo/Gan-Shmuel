<<<<<<< HEAD
from flask import Flask,
# from flask_restful import Resource, Api
=======
from flask import Flask ,jsonify
>>>>>>> a67146d2fc7e11943f7de2e9967bb21ad6345bf3

app = Flask(__name__)
@app.route("/")
def main():
    return "<h1>Test<h1>"


@app.route("/niv")
def nuv():
    return "<h1>.....<h1>"


@app.route("/health")
def is_alive():
    resp = jsonify(success=True)
    return resp
    
if  __name__ == "__main__" :
    app.run(debug=True,host="0.0.0.0", port=8080)