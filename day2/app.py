from flask import Flask, request


app = Flask(__name__)

books = [{"title": "Lean Startup", "author": "Eric Ries"}]

@app.route("/books", methods=["GET"])
def get_book_list():
    return books

@app.route("/books/<int:book_idx>", methods=["GET"])
def get_a_book(book_idx):
    return books[book_idx - 1]

@app.route("/books", methods=["POST"])
def add_book():
    title = request.form.get("title")
    author = request.form.get("author")
    books.append({
        "title": title,
        "author": author
    })

    return {}, 201

@app.route("/books/<int:book_idx>", methods=["PUT"])
def update_book(book_idx):
    title = request.form.get("title")
    author = request.form.get("author")

    book = books[book_idx - 1]
    if title:
        book["title"] = title
    
    if author:
        book["author"] = author

    books[book_idx - 1] = book

    return books

@app.route("/books/<int:book_idx>", methods=["DELETE"])
def delete_book(book_idx):
    del books[book_idx - 1]

    return books