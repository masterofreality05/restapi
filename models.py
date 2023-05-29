from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, jsonify

app = Flask(__name__)
app.app_context().push()
app.secret_key ="itsasecret"

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///cupcakes'
app.config['SQLALCHEMY_ECHO'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


db = SQLAlchemy()

def connect_db(app):
    """connects the db to the flask app"""
    db.app = app
    db.init_app(app)

connect_db(app)

class Cupcake(db.Model):
    """creates a cupcake instance"""

    __tablename__ = "cupcakes"

    def repr(self):
        """a function to facillitate better representation of class instance"""
        c = self 
        return(f"ID:{c.id}, flavor:{c.flavor}, size:{c.size},rating:{c.rating}, image:{c.image}")
    
    id = db.Column(db.Integer, autoincrement=True,
                   primary_key = True)
    
    flavor = db.Column(db.String,
                       nullable=False)
    
    size = db.Column(db.String,
                       nullable=False)
    
    rating = db.Column(db.Float,
                       nullable=False)
    
    image = db.Column(db.String,
                      default="https://tinyurl.com/demo-cupcake")


def serialize(cupcake):
    """serialize a dessert SQLAlchemy obj to dictionary"""

    return {
        "id": cupcake.id,
        "flavor": cupcake.flavor,
        "size": cupcake.size,
        "rating": cupcake.rating,
        "image": cupcake.image
    }

