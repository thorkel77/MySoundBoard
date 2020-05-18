from flask import Flask, render_template

from flask_sqlalchemy import SQLAlchemy

from passlib.hash import sha256_crypt

from models import *







import config

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'jdbc:mysql://localhost:3306/MySoundBoard'
db = SQLAlchemy(app)
app.config['SQLALCHEMY8TRACK8MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

with app.app_context():
    db.init_app(app)



@app.route('/login', methods = ['GET', 'POST'])
def login():
    if request.method == "POST":
        username = request.form['inputUsername']
        password = request.form['inputPassword']

        usr = db.session.query(Users).filter(Users.username == username).first()
        if usr and sha256_crypt.verify(password, usr.password):
            session['id_user'] = id_user
            return redirect(url_for("home"))
        else:
            flash(f"password or username are incorrect.", "info")
    return render_template("login.html")




@app.route('/inscription')
def inscription():
	return render_template('inscription.html')



@app.route('/')
def home():
	return render_template('home.html')


@app.route('/profil')
def profil():
    return render_template('profil.html')

if __name__== '__main__':

    app.run(debug=True)