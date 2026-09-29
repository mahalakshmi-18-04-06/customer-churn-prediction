# Customer Churn Prediction

A Machine Learning web application that predicts whether a customer is likely to churn based on their service usage, contract, and billing information.

## Project Overview

Customer churn refers to customers discontinuing a service.

This project uses Machine Learning to analyze customer information and predict whether a customer is likely to churn or not.

The trained Machine Learning model is integrated with a Flask web application where users can enter customer details and receive a churn prediction.

## Model Performance

- Model Accuracy: 78.46%
- Prediction Type: Binary Classification
- Output:
  - Customer is likely to churn
  - Customer is not likely to churn

## Features Used

The application accepts customer information such as:

- Gender
- Senior Citizen
- Partner
- Dependents
- Tenure
- Phone Service
- Multiple Lines
- Internet Service
- Online Security
- Online Backup
- Device Protection
- Tech Support
- Streaming TV
- Streaming Movies
- Contract
- Paperless Billing
- Payment Method
- Monthly Charges
- Total Charges

## Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- Flask
- HTML
- CSS
- Jupyter Notebook
- GitHub

## Project Structure

```text
Customer-Churn-Prediction/
│
├── dataset/
│
├── model/
│   ├── churn_model.pkl
│   ├── scaler.pkl
│   └── features.pkl
│
├── notebook/
│   ├── Customer_Churn_Prediction_Final.ipynb
│   └── Customer_Churn_Prediction.ipynb
│
├── static/
│   └── style.css
│
├── templates/
│   └── index.html
│
├── app.py
├── requirements.txt
└── README.md