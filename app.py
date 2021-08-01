from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime



app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:om2694oM@localhost/postgres"
db=SQLAlchemy(app)
class Cable (db.Model):
    __tablename__ = 'cables'
    product_number=db.Column(db.Integer, primary_key=True)
    family = db.Column(db.Integer, unique=True, nullable=False)
    frequency = db.Column(db.Integer, unique=True,nullable=False)

    def __repr__(self):
        return "details:("+str(self.product_number)+","+str(self.frequency)+")"

@app.route("/")
@app.route("/main")
def home():
    cables = Cable.query.all()
    
    return render_template('main.html', cables=cables)



   # string = str(Cable.query.all())
    #return string



if __name__=='__main__':
  app.run(debug=True)

