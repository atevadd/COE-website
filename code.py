from flask import Flask, render_template, redirect, url_for, request, flash
from flask_sqlalchemy import SQLAlchemy
from mail_sender import mailer

app = Flask(__name__)
app.config['SECRET_KEY'] = ',,\xf5y\xd6\xea\xa9#HDo\x86\x8d\xd2\x18<\xac\x10\x81\r\xda\x85\xe7\xb9'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:atevadd@localhost:3306/coe'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


db = SQLAlchemy(app)

class Prayer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    request = db.Column(db.String(300), nullable=False)

    def __repr__(self):
        return '<User %r>' % self.name

class Mail(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(80), nullable=False)


@app.route("/")
@app.route("/Index", methods=['GET', 'POST'])
def index():
    if request.method == "POST":
        name = request.form["name"]
        prayer = request.form['prayer']
        if name == '' or prayer == '':
            flash("Enter the request field")
            return redirect(url_for('index'))
        else:
            data = Prayer(name=name, request=prayer)
            db.session.add(data)
            db.session.commit()
            mailer(name, prayer)
            flash("Prayer Request Sent Successfully")
            return redirect(url_for('index'))
    return render_template('index.html')


@app.route("/About/<string:mess>", methods=["GET", "POST"])
def about(mess):
    if request.method == 'POST':





        
        email = request.form['email']
        if email == '':
            # flash('Enter a valid Email')
            return redirect(url_for('index', mess="Subscription Successfully"))
        else:
            data = Mail(email=email)
            db.session.add(data)
            db.session.commit()
            # flash("Subscription successful")
            return redirect(url_for('index',  mess="Subscription Successfully"))
    return render_template('about.html')

@app.route("/Events")
def event():
    return render_template('events.html')


@app.route("/FAQs")
def faqs():
    return render_template('faqs.html')


if __name__ == "__main__":
    app.run()
