from flask import Flask, render_template
import requests
import datetime

app = Flask(__name__)

def fetch_db():
    response = requests.get("https://api.npoint.io/0e426d8e041755486740")
    response.raise_for_status()
    return response.json()

@app.route('/')
def home():
    today = datetime.datetime.today()
    return render_template("index.html", posts=fetch_db(), today=today)

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route('/post/<int:id>')
def post(id):
    data_base = fetch_db()
    today = datetime.datetime.today()
    post = next((p for p in data_base if p['id'] == id), None)
    if post is None:
        return "Post not found", 404
    return render_template("post.html", id=id, post=post, today=today)


if __name__ == '__main__':
    app.run(debug=True)
