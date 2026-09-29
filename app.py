from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)

# Load saved files
model = pickle.load(open("model/churn_model.pkl", "rb"))
scaler = pickle.load(open("model/scaler.pkl", "rb"))
features = pickle.load(open("model/features.pkl", "rb"))

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():

    # Read values from form
    gender = request.form["gender"]
    senior = int(request.form["SeniorCitizen"])
    partner = request.form["Partner"]
    dependents = request.form["Dependents"]
    tenure = int(request.form["tenure"])
    phoneservice = request.form["PhoneService"]
    multiplelines = request.form["MultipleLines"]
    internetservice = request.form["InternetService"]
    online_security = request.form["OnlineSecurity"]
    online_backup = request.form["OnlineBackup"]
    device_protection = request.form["DeviceProtection"]
    tech_support = request.form["TechSupport"]
    streaming_tv = request.form["StreamingTV"]
    streaming_movies = request.form["StreamingMovies"]
    contract = request.form["Contract"]
    paperless = request.form["PaperlessBilling"]
    payment = request.form["PaymentMethod"]
    monthly = float(request.form["MonthlyCharges"])
    total = float(request.form["TotalCharges"])

    # Create dictionary
    input_dict = {
        "gender": gender,
        "SeniorCitizen": senior,
        "Partner": partner,
        "Dependents": dependents,
        "tenure": tenure,
        "PhoneService": phoneservice,
        "MultipleLines": multiplelines,
        "InternetService": internetservice,
        "OnlineSecurity": online_security,
        "OnlineBackup": online_backup,
        "DeviceProtection": device_protection,
        "TechSupport": tech_support,
        "StreamingTV": streaming_tv,
        "StreamingMovies": streaming_movies,
        "Contract": contract,
        "PaperlessBilling": paperless,
        "PaymentMethod": payment,
        "MonthlyCharges": monthly,
        "TotalCharges": total
    }

    # Convert to one-hot encoded dataframe
    import pandas as pd

    df = pd.DataFrame([input_dict])

    df = pd.get_dummies(df)

    # Match training columns
    df = df.reindex(columns=features, fill_value=0)

    # Scale
    df_scaled = scaler.transform(df)

    # Prediction
    prediction = model.predict(df_scaled)[0]

    if prediction == 1:
        result = "Customer is likely to Churn."
    else:
        result = "Customer is Not Likely to Churn."

    return render_template("index.html", prediction_text=result)


if __name__ == "__main__":
    app.run(debug=True)