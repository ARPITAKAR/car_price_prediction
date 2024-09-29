import pandas as pd
import joblib
from flask import (
    Flask,
    url_for,
    render_template
)
from forms import InputForm

app = Flask(__name__)
app.config["SECRET_KEY"] = "secret_key"

model = joblib.load("model.joblib")

@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html", title="Home")



@app.route("/predict", methods=["GET", "POST"])
def predict():
    form = InputForm()
    if form.validate_on_submit():
        # Correctly creating the DataFrame
        input_data = pd.DataFrame(
            dict(
                Age=[form.Age.data],
                brand=[form.brand.data],
                milage=[form.Milage.data],
                fuel_type=[form.fuel_type.data],
                ext_col=[form.ext_col.data],
                int_col=[form.int_col.data],
                accident=[form.accident.data],
                clean_title=[form.clean_title.data],
                horsepower=[form.horsepower.data],
                engine_capacity=[form.engine_capacity.data],
                cylinders=[form.cylinders.data]
            )
        )

        # Convert 'accident' to float and then to int
        input_data['accident'] = input_data['accident'].astype(float).astype(int)

        # Get the model prediction
        prediction = model.predict(input_data)
        
        # Format the prediction as a message
        message = f"Predicted price: {prediction[0]:.0f} INR!"
    else:
        message = "Please provide valid input details!"

    return render_template("predict.html", title="Predict", form=form, output=message)


if __name__ == "__main__":
    app.run(debug=True)