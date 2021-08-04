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
    family = db.Column(db.Integer, unique=True, nullable=False)
    frequency = db.Column(db.Integer, unique=True, nullable=False)
    diameter = db.Column(db.Integer, unique=True, nullable=False)

    def __repr__(self):
        return "{\"product_number\":" + str(self.product_number) +\
               ",\"frequency\":" + str(self.frequency) + "}"


@app.route("/")
@app.route("/main")
def home():
    return render_template('main.html')


@app.route("/filter")
def filer():
    length = request.args.get('length')
    frequency = request.args.get('frequency')
    diameter = request.args.get('diameter')
    # cables = Cable.query.all()
    cables = Cable.query.filter_by(Cable.frequency > frequency, Cable.diameter == diameter).first()

    # result = db.engine.execute(text("SELECT * FROM cables;").execution_options(autocommit=True))
    # result = Cable.query.filter_by(length=length).first()
    # return str(result);
    return str(cables);
    # return json.loads(to_json(result, Cable))


def to_json(inst, cls):
    """
    Jsonify the sql alchemy query result.
    """
    convert = dict()
    # add your coversions for things like datetime's
    # and what-not that aren't serializable.
    d = dict()
    for c in cls.__table__.columns:
        v = getattr(inst, c.name)
        if c.type in convert.keys() and v is not None:
            try:
                d[c.name] = convert[c.type](v)
            except:
                d[c.name] = "Error:  Failed to covert using ", str(convert[c.type])
        elif v is None:
            d[c.name] = str()
        else:
            d[c.name] = v
    return json.dumps(d)


if __name__ == '__main__':
    app.run(debug=True)
