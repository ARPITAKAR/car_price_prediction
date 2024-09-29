import pandas as pd
from flask_wtf import FlaskForm
from wtforms import (
    SelectField,
    DateField,
    TimeField,
    IntegerField,
    SubmitField
)
from wtforms.validators import DataRequired

# getting the data
df = pd.read_csv("output.csv")

class InputForm(FlaskForm):
    Age = IntegerField(
        label="Model_years_passed",
        validators=[DataRequired()]
    )

    brand = SelectField(
        label="Company car",
        choices=df.brand.unique().tolist(),
        validators=[DataRequired()]
    )

    Milage = IntegerField(
        label="Milage in 10000",
        validators=[DataRequired()]
    )

    fuel_type = SelectField(
        label="Type of fuel",
        choices=df.fuel_type.unique().tolist(),
        validators=[DataRequired()]
    )

    ext_col = SelectField(
        label="External color",
        choices=df.ext_col.unique().tolist(),
        validators=[DataRequired()]
    )

    int_col = SelectField(
        label="Internal color",
        choices=df.int_col.unique().tolist(),
        validators=[DataRequired()]
    )

    accident = SelectField(
        label="Accident met",
        choices=df.accident.unique().tolist(),
        validators=[DataRequired()]
    )

    clean_title = SelectField(
        label="Title clean",
        choices=df.clean_title.unique().tolist(),
        validators=[DataRequired()]
    )

    horsepower= IntegerField(
        label="horsepower",
        validators=[DataRequired()]
    )

    engine_capacity = IntegerField(
        label="engine_capacity",
        validators=[DataRequired()]
    )

    # Load choices dynamically
    cylinders = IntegerField(
        label="cylinder_capacity",
        validators=[DataRequired()]
    )

    submit = SubmitField("Car Price")