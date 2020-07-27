from flask import Flask ,jsonify
from flask.ext.mysql import MySQL
from healthcheck import HealthCheck, EnvironmentDump
from flask_sqlalchemy import SQLAlchemy
# from sqlalchemy import MetaData

# For the docker file flask app: (DO NOT DELETE!)
# pip install Flask , or, pip install -U Flask (version 1.1.2)
# pip install Flask-MySQL  (version 1.5.1)
# pip install healthcheck (version 1.3.3)
# pip install Flask-SQLAlchemy (version 2.4.4)
# pip install SQLAlchemy (version 1.3.18)


app = Flask(__name__)
health = HealthCheck(app, "/healthcheck")
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://mylogin:mypw@localhost/mydb'
db = SQLAlchemy(app)

@app.route("/")
def main():
    return "<h1>This is Flask frontend webapp Test!<h1>"


# Niv def





# Mor def
@app.route("/health")
def is_alive():
    resp = jsonify(success=True)
    return resp
    
if  __name__ == "__main__" :
    app.run(debug=True,host="localhost", port=8089)