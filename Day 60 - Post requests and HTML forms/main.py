
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/login', methods=["POST"])
def submit():
    fname = request.form["fname"]
    lname = request.form["lname"]
    print("success")
    return f"Hello, {fname} {lname}!"
if __name__ == '__main__':
    app.run(debug=True)
