from flask import Flask,render_template
from flight import registerform

app=Flask(__name__)
app.config['SECRET_KEY']='232323'
@app.route('/')
@app.route("/home")
def home():
    return render_template("home.html",title="home")


@app.route("/about")
# def about():
#     return render_template("about.html",title="about")

@app.route("/register")
def register():
    form=registerform()
    return render_template("flightregister.html",form=form)

if __name__=='__main__':
    app.run(debug=True)

