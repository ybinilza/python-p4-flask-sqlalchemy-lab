from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData, DateTime

metadata = MetaData(naming_convention={
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
})

db = SQLAlchemy(metadata=metadata)

class Zookeeper(db.Model):
    __tablename__ = 'zookeepers'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    birthday = db.Column(DateTime)

    #animals = db.relationship('Animal', backref='zookeepers')

class Enclosure(db.Model):
    __tablename__ = 'enclosures'

    id = db.Column(db.Integer, primary_key=True)
    enviorment = db.Column(db.String)
    open_to_visitors = db.Column(db.Boolean)

    #animals = db.relationship('Animal', backref='enclosures')

class Animal(db.Model):
    __tablename__ = 'animals'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    species = db.Column(db.String)
    
    #zookeeper = db.relationship('Zookeeper', backref='animal')
    #enclosure = db.relationship('Enclosure', backref='animal')

    def __repr__(self):
        return f'<Animal {self.name}>'