from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, FloatField
from wtforms import validators


class CreateClothes(FlaskForm):
    style_name = StringField("Name: ", [
        validators.DataRequired("Please enter clothes Name.")
])
outwear = StringField("Outwear: ", [
        validators.DataRequired("Please enter clothes Outwear.")
])
lowerwear = StringField("Lowerwear: ", [
        validators.DataRequired("Please enter clothes Lowerwear.")
])
shoes = StringField("Shoes: ", [
        validators.DataRequired("Please enter clothes Shoes.")
])
options_id = IntegerField("Options id: ", [
        validators.DataRequired("Please enter clothes Options id.")
 ])
submit = SubmitField("Save")


class EditClothes(FlaskForm):
    style_name = StringField("Name: ", [
        validators.DataRequired("Please enter clothes Name.")
])
outwear = StringField("Outwear: ", [
        validators.DataRequired("Please enter clothes Outwear.")
])
lowerwear = StringField("Lowerwear: ", [
        validators.DataRequired("Please enter clothes Lowerwear.")
])
shoes = StringField("Shoes: ", [
        validators.DataRequired("Please enter clothes Shoes.")
])
submit = SubmitField("Save")