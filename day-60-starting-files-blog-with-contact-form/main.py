from flask import Flask, render_template, request
import requests
from datetime import datetime

# USE YOUR OWN npoint LINK! ADD AN IMAGE URL FOR YOUR POST. 👇
posts = requests.get("https://api.npoint.io/0e426d8e041755486740").json()

app = Flask(__name__)

@app.context_processor
def inject_full_date():
    full_date = datetime.now().strftime("%A, %B %d, %Y")  # Example: Wednesday, May 29, 2025
    return {'current_date': full_date}

@app.route('/')
def get_all_posts():
    return render_template("index.html", all_posts=posts)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html", subheading="Contact me")


@app.route("/post/<int:index>")
def show_post(index):
    requested_post = None
    for blog_post in posts:
        if blog_post["id"] == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)


@app.route("/form-entry" ,methods=['POST'])
def receive_data():
    print (request.form["name"])
    print(request.form["email"])
    print(request.form["phone"])
    print(request.form["message"])
    return render_template("contact.html", subheading="I successfully received your message!")


if __name__ == "__main__":
    app.run(debug=True, port=5001)
