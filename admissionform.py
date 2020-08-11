from flask import Flask,render_template,redirect,url_for
from application import registerform
from flask_sqlalchemy import SQLAlchemy

app=Flask(__name__)
app.config['SECRET_KEY']='1234'
app.config['SQLALCHEMY_DATABASE_URI']="postgresql://postgres:123@localhost:5432/Blogdb"
db=SQLAlchemy(app)
@app.route('/')
@app.route("/home")
def home():
    return render_template("home.html",title="home")


@app.route("/about")
# def about():
#     return render_template("about.html",title="about")

@app.route("/register",methods=["post","GET"])
def register1():
    form=registerform()
    if form.validate_on_submit():
        title="about-"+str(form.first_name)
        return redirect(url_for('home'))
    return render_template("applicationform.html",form=form)

if __name__=='__main__':
    app.run(debug=True)

