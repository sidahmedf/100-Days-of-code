from flask_bootstrap import Bootstrap5
from flask import Flask, render_template
from form import MyForm
import secrets

'''
Red underlines? Install the required packages first: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
'''


app = Flask(__name__)
app.config['SECRET_KEY'] = secrets.token_hex(32)
bootstrap = Bootstrap5(app)

@app.route("/")
def home():
    return render_template('index.html')


@app.route("/login", methods=['GET', 'POST'])
def login() :
    form = MyForm()
    if form.validate_on_submit():
        if form.email.data =='admin@email.com' and form.pwd.data == '12345678':
                return render_template("success.html")

        return render_template("denied.html")

    return render_template("login.html", form=form)

if __name__ == '__main__':
    app.run(debug=True)
