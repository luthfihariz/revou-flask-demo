from flask import Flask, request
import string

app = Flask(__name__)

@app.route("/")
def index():
    print(request.base_url)
    print(request.endpoint)
    print(request.headers)
    print(request.args)
    return 'Hello world'

@app.route("/dummy")
def dummy():
    return {"error":"Token is not valid!"}, 403 # Response Object