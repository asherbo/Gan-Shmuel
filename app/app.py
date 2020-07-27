from flask import Flask ,jsonify
from flask.ext.mysql import MySQL
from healthcheck import HealthCheck, EnvironmentDump
# from flask_sqlalchemy import SQLAlchemy
# from sqlalchemy import MetaData

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db = SQLAlchemy(app)

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
    app.run(debug=True,host="localhost", port=8089)