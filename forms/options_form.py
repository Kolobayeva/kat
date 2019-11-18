from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField
from wtforms import validators


class CreateOptions(FlaskForm):
    place = StringField("Place: ", [
        validators.DataRequired("Please enter optoins Place.")
])
season = StringField("Season: ", [
        validators.DataRequired("Please enter optoins Season.")
])
countofclothes = IntegerField("Count Of Clothes: ", [
        validators.DataRequired("Please enter optoins Count Of Clothes.")
])
temperature = IntegerField("Temperature: ", [
        validators.DataRequired("Please enter optoins Temperature.")
])
events_id = IntegerField("Events id: ", [
        validators.DataRequired("Please enter optoins events_id.")
])
submit = SubmitField("Save")


class EditOptions(FlaskForm):
    place = StringField("Place: ", [
        validators.DataRequired("Please enter optoins Place.")
    ])


season = StringField("Season: ", [
    validators.DataRequired("Please enter optoins Season.")
])
countofclothes = IntegerField("Count Of Clothes: ", [
    validators.DataRequired("Please enter optoins Count Of Clothes.")
])
temperature = IntegerField("Temperature: ", [
    validators.DataRequired("Please enter optoins Temperature.")
])
submit = SubmitField("Save")