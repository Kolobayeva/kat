import os

from flask import Flask, request, render_template, redirect, url_for

from connecting.credentials import *
from model.model import db, QuestionsTable, AnswerTable, QuestionnaireTable, StudentTable, WorkTable, StudentHasWork, \
    CarsTable
from forms.QuestionForm import QuestionForm
from forms.AnswerForm import AnswerForm
from forms.QuestionnaireForm import QuestionnaireForm
from forms.StudentForm import StudentForm
from forms.WorkForm import WorkForm
from forms.StudentHasWorkForm import StudentHasWorkForm
from forms.CarsForm import CarsForm
from model.vizualization import visualization_data

app = Flask(__name__)
app.secret_key = 'development key'

app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL",
                                                  f"postgresql://{username}:{password}@{hostname}:{port}/{database_name}")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)


@app.route('/')
def root():
    db.create_all()
    return render_template("main.html")


@app.route('/map')
def map():
    db.create_all()

    student_1 = StudentTable(Student_name='Bob',
                             Student_surname='Bobov')
    student_2 = StudentTable(Student_name='Boba',
                             Student_surname='Bobenko')
    student_3 = StudentTable(Student_name='Bobik',
                             Student_surname='Bobenchuk')

    car_1 = CarsTable(Model='BMW',
                      Cost='1000',
                      Number='123456',
                      Color='Red',
                      StudentCardFk=2
                      )

    car_2 = CarsTable(Model='Audi',
                      Cost='750',
                      Number='987654',
                      Color='Green',
                      StudentCardFk=2
                      )

    car_3 = CarsTable(Model='Nissan',
                      Cost='200',
                      Number='888888',
                      Color='Red',
                      StudentCardFk=3
                      )

    # db.session.add_all([student_1, student_2, student_3])
    db.session.add_all([car_1, car_2, car_3])
    db.session.commit()
    return render_template("main.html")
