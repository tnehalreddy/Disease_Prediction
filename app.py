from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__, static_folder="static")

# Load your machine learning models
diabetes_model = pickle.load(open("diabetes_model.sav", "rb"))
heart_disease_model = pickle.load(open("heart_disease_model.sav", "rb"))


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/predict_diabetes", methods=["POST"])
def predict_diabetes():
    if request.method == "POST":
        # Retrieve form data
        int_features = [float(x) for x in request.form.values()]
        final_features = [np.array(int_features)]

        # Perform prediction using the loaded model
        prediction_diabetes = diabetes_model.predict(final_features)
        output = "diabetic" if prediction_diabetes[0] == 1 else "not diabetic"

        # Generate suggestions based on input values
        suggestions = generate_diabetes_suggestions(int_features)

        return render_template(
            "index.html",
            diabetes_prediction_text="The person is {}".format(output),
            suggestions=suggestions,
        )


@app.route("/predict_heart_disease", methods=["POST"])
def predict_heart_disease():
    if request.method == "POST":
        # Retrieve form data and convert to integers
        int_features = [float(x) for x in request.form.values()]

        # Perform prediction using the loaded model
        prediction = heart_disease_model.predict([int_features])
        output = (
            "is having heart disease"
            if prediction == 1
            else "does not have any heart disease"
        )

        # Generate suggestions based on input values
        suggestions = generate_heart_disease_suggestions(int_features)

        return render_template(
            "index.html",
            heart_prediction_text="The person {}".format(output),
            suggestions2=suggestions,
        )


def generate_diabetes_suggestions(features):
    pregnancies, glucose, blood_pressure, skin_thickness, insulin, bmi, dpf, age = (
        features
    )
    suggestions = []
    if pregnancies > 3:
        suggestions.append(
            "High number of pregnancies may increase the risk of gestational diabetes. Consult a healthcare professional."
        )
    if glucose > 150:
        suggestions.append(
            "Your glucose level is high. Please consult a healthcare professional for advice."
        )
    if 25 < bmi < 30:
        suggestions.append(
            "Your BMI is in the overweight range. Consider maintaining a healthy weight through a balanced diet and regular exercise."
        )
    if age > 40:
        suggestions.append(
            "Individuals over 40 are at a higher risk of developing diabetes. Monitor your health and consult a doctor."
        )
    if blood_pressure > 130:
        suggestions.append(
            "High blood pressure can contribute to diabetes complications. Monitor your blood pressure regularly."
        )
    elif blood_pressure < 90:
        suggestions.append(
            "Low blood pressure may indicate other health issues. Consult with a healthcare professional."
        )
    if skin_thickness > 25:
        suggestions.append(
            "High skin thickness may be associated with insulin resistance. Maintain a healthy lifestyle."
        )
    if insulin > 150:
        suggestions.append(
            "Elevated insulin levels may indicate insulin resistance. Consult with a healthcare professional."
        )
    if dpf > 0.8:
        suggestions.append(
            "High Diabetes Pedigree Function indicates a genetic predisposition to diabetes. Regular monitoring is advised."
        )
    return suggestions


def generate_heart_disease_suggestions(features):
    (
        age,
        sex,
        cp,
        trestbps,
        chol,
        fbs,
        restecg,
        thalach,
        exang,
        oldpeak,
        slope,
        ca,
        thal,
    ) = features
    suggestions = []
    if age > 50:
        suggestions.append(
            "Individuals over 50 should monitor their heart health regularly."
        )
    elif age < 30:
        suggestions.append(
            "Maintain a healthy lifestyle to prevent early onset of heart issues."
        )
    if chol > 200:
        suggestions.append(
            "High cholesterol levels may increase the risk of heart disease. Consult a healthcare professional."
        )
    if trestbps > 140:
        suggestions.append(
            "High blood pressure can lead to heart complications. Monitor your blood pressure regularly."
        )
    elif trestbps < 90:
        suggestions.append(
            "Low blood pressure may indicate other health issues. Consult with a healthcare professional."
        )
    if thalach < 60:
        suggestions.append(
            "Low heart rate may indicate bradycardia. Consult with a healthcare professional."
        )
    elif thalach > 100:
        suggestions.append(
            "High heart rate may indicate tachycardia. Consult with a healthcare professional."
        )
    return suggestions


if __name__ == "__main__":
    app.run(debug=True)
