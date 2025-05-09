from flask import Flask, render_template
import requests


app = Flask(__name__)

def fetch_db():
    response = requests.get("https://api.npoint.io/c790b4d5cab58020d391")
    response.raise_for_status()
    return response.json()

@app.route('/')
def home():
    return render_template("index.html", posts=fetch_db())

@app.route('/post/<int:id>')
def post(id):
    data_base=fetch_db()
    return render_template("post.html", id=id, post=data_base[id])

if __name__ == "__main__":
    app.run(debug=True)
