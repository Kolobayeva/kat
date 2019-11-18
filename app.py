from flask import Flask, request, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import func, text
import json
from sqlalchemy import Column, Integer, String, Date, ForeignKey, DateTime, Text, CheckConstraint, Sequence, Float, UniqueConstraint
from sqlalchemy.orm import relationship
import datetime
from forms.events_form import CreateEvents, EditEvents
from forms.options_form import CreateOptions, EditOptions
from forms.user_form import CreateUser, EditUser
from forms.clothes_form import CreateClothes, EditClothes
import plotly
import plotly.graph_objs as go

app = Flask(__name__)
app.secret_key = 'key'

ENV = 'prod'

if ENV == 'dev':
    app.debug = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:1111@localhost/kolobayeva'
else:
    app.debug = False
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://qexacebxlyoflv:7f1848d692d8a690603199584eaf0f697e63459f365c69074da6ec8ca508e9fc@ec2-107-21-126-201.compute-1.amazonaws.com:5432/ddj3djvlda7rga'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class ormUsers(db.Model):
    __tablename__ = 'users'
    id = Column(Integer, Sequence('users_id_seq', start=1, increment=1), primary_key=True)
    login = Column(String(30), UniqueConstraint(name = 'users_login_key') ,nullable=False)
    password = Column(String(50), nullable=False)
    email = Column(String(50), UniqueConstraint(name = 'users_email_key') ,nullable=False)
    lastname = Column(String(30))
    firstname = Column(String(30))
    Age = Column(Integer)
    Eyes = Column(String(30))
    Hair = Column(String(30))
    Height = Column(Integer)
    created = Column(DateTime, default=datetime.datetime.now())
    userRelationShip = relationship("ormEvents", back_populates="user_Relation_Ship")

class ormEvents(db.Model):
    __tablename__ = 'Events'
    id = Column(Integer, Sequence('Events_id_seq', start=1, increment=1), primary_key=True)
    event_name = Column(String(30), nullable=False)
    created = Column(DateTime, default=datetime.datetime.now())
    countofoptions = Column(Integer, CheckConstraint('countofoptions >= 0'), nullable=False, default=0)
    user_id = Column(Integer, ForeignKey('users.id'))
    user_Relation_Ship = relationship("ormUsers", back_populates="userRelationShip")
    EventsRelationShip = relationship("ormOptions", back_populates="Events_Relation_Ship")

class ormOptions(db.Model):
    __tablename__ = 'options'
    id = Column(Integer, Sequence('options_id_seq', start=1, increment=1), primary_key=True)
    place = Column(String(30), nullable=False)
    season = Column(String(30))
    created = Column(DateTime, default=datetime.datetime.now())
    temperature = Column(Integer)
    countofclothes = Column(Integer, CheckConstraint('countofclothes >= 0'), nullable=False, default=0)
    Events_id = Column(Integer, ForeignKey('Events.id'))
    Events_Relation_Ship = relationship("ormEvents", back_populates="EventsRelationShip")
    ClothesRelationShip = relationship("ormClothes", back_populates="Clothes_Relation_Ship")

class ormClothes(db.Model):
    __tablename__ = 'clothes'
    id = Column(Integer, Sequence('options_id_seq', start=1, increment=1), primary_key=True)
    style_name = Column(String(30), nullable=False)
    outwear = Column(String(30))
    lowerwear = Column(String(30))
    shoes = Column(String(30))
    created = Column(DateTime, default=datetime.datetime.now())
    countofclothes = Column(Integer, CheckConstraint('countofclothes >= 0'), nullable=False, default=0)
    options_id = Column(Integer, ForeignKey('options.id'))
    Clothes_Relation_Ship = relationship("ormOptions", back_populates="ClothesRelationShip")

@app.route('/')
def hello_world():
    text = ""
    return render_template('index.html', action="/")
@app.route('/all/user')
def all_user():
    name = "user"
    user_db = db.session.query(ormUsers).all()
    user = []
    for row in user_db:
        user.append({"id": row.id, "login": row.login, "password": row.password, "email": row.email,
                     "lastname": row.lastname, "firstname": row.firstname, "age": row.age,"eyes": row.eyes, "hair": row.hair, "height": row.height,"created": row.created})
    return render_template('allUser.html', name=name, users=user, action="/all/user")

@app.route('/all/events')
def all_events():
    name = "events"
    events_db = db.session.query(ormEvents).all()
    events = []
    for row in events_db:
        events.append({"id": row.id, "name": row.event_name, "event_date": row.event_date, "created": row.created,
                           "countofoptions": row.countofoptions, "user_id": row.user_id})
    return render_template('allEvents.html', name=name, events=events, action="/all/events")

@app.route('/all/options')
def all_options():
    name = "options"
    options_db = db.session.query(ormOptions).all()
    options = []
    for row in options_db:
        options.append({"id": row.id, "place": row.place, "season ": row.season , "created": row.created, "temperature": row.temperature,
                        "countofclothes": row.countofclothes, "Events_id": row.Events_id})
    return render_template('allOptions.html', name=name, options=options, action="/all/options")

@app.route('/all/clothes')
def all_clothes():
    name = "clothes"
    clothes_db = db.session.query(ormClothes).all()
    clothes = []
    for row in clothes_db:
        clothes.append({"id": row.id, "name": row.style_name, "outwear": row.outwear, "lowerwear": row.lowerwear, "shoes": row.shoes,
                     "created": row.created, "rating": row.rating, "options_id": row.options_id})
    return render_template('allClothes.html', name=name, clothes=clothes, action="/all/clothes")

if __name__ == '__main__':
    app.run()