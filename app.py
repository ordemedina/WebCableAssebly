import json
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

from sqlalchemy import text

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:om2694oM@localhost/postgres"
db = SQLAlchemy(app)


class Cable(db.Model):
    __tablename__ = 'cables'
    product_number = db.Column(db.Integer, primary_key=True)
    family = db.Column(db.Integer, unique=False, nullable=False)
    frequency = db.Column(db.Integer, unique=False, nullable=False)
    diameter = db.Column(db.Integer, unique=False, nullable=False)

    def __repr__(self):
        return "{\"product_number\":\"" + str(self.product_number) + "\"" +\
               ",\"family\":" + str(self.family) +\
               ",\"frequency\":" + str(self.frequency) +\
               ",\"diameter\":" + str(self.diameter) +\
               + "}"


class Connector(db.Model):
    __tablename__ = 'connectors'
    var1 = db.Column(db.Integer, primary_key=True)
    var2 = db.Column(db.Integer, unique=True, nullable=False)

    def __repr__(self):
        return "{\"var1\":\"" + str(self.var1) + "\"" +\
               ",\"var2\":" + str(self.var2) +\
               + "}"


@app.route("/")
@app.route("/main")
def home():
    return render_template('main.html')


@app.route("/filter-cable")
def filer_cable():
    # Get all the parameter from the url (?length=10&freq....)
    length = request.args.get('length')
    frequency = request.args.get('frequency')
    diameter = request.args.get('diameter')
    # cables = Cable.query.all()
    query_result = Cable.query.filter_by(Cable.frequency > frequency, Cable.diameter == diameter)
    return str(query_result)



@app.route("/filter-connector")
def filer_connector():
    var1 = request.args.get('var1')
    var2 = request.args.get('var2')
    # cables = Cable.query.all()
    query_result = Connector.query.filter_by(Connector.var1 > var1, Connector.var2 == var2).first()
    return str(query_result)



if __name__ == '__main__':
    app.run(debug=True)
