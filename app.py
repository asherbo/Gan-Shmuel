from flask import Flask

app = Flask(__name__)
@app.route("/")
def main():
    return "<h1>mor bargig !<h1>"

@app.route("/niv")
def nuv():
    return "<h1>niv gabay !<h1>"

    
if  __name__ == "__main__" :
    app.run(debug=True,host="localhost", port=8080)