from flask import Flask,
# from flask_restful import Resource, Api

app = Flask(__name__)
@app.route("/")
def main():
    return "<h1>Test<h1>"


@app.route("/niv")
def nuv():
    return "<h1>.....<h1>"

    
if  __name__ == "__main__" :
    app.run(debug=True,host="0.0.0.0", port=8080)