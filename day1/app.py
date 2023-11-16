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


book_list = [{'title': 'Dummy Book Title', 'author': 'Luthfi Hariz'}]

@app.route("/books", methods=["GET", "POST"])
def handle_books():
    if request.method == "GET":
        return book_list
    else:
        title = request.form.get('title')
        author = request.form.get('author')
        book_list.append({
            'title': title,
            'author': author
        })
        return {}, 201