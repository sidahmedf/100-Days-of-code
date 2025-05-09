from flask import Flask
from decorator import *

app = Flask(__name__)

@app.route("/")
def hello_world():
    return '<h1 style="text-align:center;color:red">Hello Sidahmed</h1>' \
           '<p style="text-align:center">This is a paragraph</p>'\
           '<img src="https://media3.giphy.com/media/v1.Y2lkPTc5MGI3NjExazEwYm1jZ2F6bnR1cmN4cWlveXdpZDViendwYW40bHAwcGk5a3djMSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/QBGfW8HqzXzYDojCqo/giphy.gif" style="display: block; margin: auto;" alt="Centered Image">>'


@app.route("/karim")
@make_bold
@make_emphesis
@make_underlines
def karim() :
    return "Karim"

@app.route("/<name>/<int:number>")
def name(name, number):
    return f"Welcome {name}, you are visiting page {number}"

if __name__ == "__main__" :
    app.run(debug=True)