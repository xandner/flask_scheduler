from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import datetime

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///test.sqlite"
db = SQLAlchemy(app)


class Test(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    test_sch = db.Column(db.String)
db.create_all()

@app.cli.command()
def scheduled():
    db.session.add(Test(test_sch=str(datetime.datetime.now())))
    db.session.commit()


@app.route("/")
def home():
    return "Welcome Home :) !"

if __name__ == "__main__":
    app.run()
