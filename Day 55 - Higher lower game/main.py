from decorator import *
from flask import Flask
from random import choice

app = Flask(__name__)

random_number = choice([i for i in range(0,9)])

@app.route("/")
def hello():
    return (render_h1("Guess a number between 0 and 9")+
            render_image("https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif"))


@app.route("/<int:number>")
def main(number) :
    if random_number>number :
        return (render_h1("Too low, try again!")+
                render_image("https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif"))
    if random_number<number :
        return render_h1("Too high, try again!")+render_image("https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif")
    else:
        return render_h1("You found me!")+render_image("https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif")


if __name__ == "__main__" :
    app.run(debug=True)