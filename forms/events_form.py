from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField
from wtforms import validators


class CreateEvents(FlaskForm):
    event_name = StringField("Name: ", [
        validators.DataRequired("Please enter events Name.")

    ])
    event_date = StringField("Date: ", [
        validators.DataRequired("Please enter events  Date.")

    ])

    countofevents = IntegerField("Count Of Events: ", [
        validators.DataRequired("Please enter events Count Of Events.")

    ])
    user_id = IntegerField("User id: ", [
        validators.DataRequired("Please enter events User id.")

    ])
    submit = SubmitField("Save")


class EditEvents(FlaskForm):
    event_name = StringField("Name: ", [
        validators.DataRequired("Please enter events Name.")

    ])
    event_date = StringField("Date: ", [
        validators.DataRequired("Please enter events  Date.")

    ])

    countofevents = IntegerField("Count Of Events: ", [
        validators.DataRequired("Please enter events Count Of Events.")
		   ])


    submit = SubmitField("Save")
