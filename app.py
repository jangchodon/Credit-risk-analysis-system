
import streamlit as st
import joblib
import pandas as pd

model = joblib.load("credit_risk_model.pkl")

st.title("Credit Risk Analysis System")

dependents = st.number_input("Number of Dependents", min_value=0)
income = st.number_input("Annual Income", min_value=0)
loan_amount = st.number_input("Loan Amount", min_value=0)
loan_term = st.number_input("Loan Term", min_value=0)
cibil_score = st.number_input("CIBIL Score", min_value=300, max_value=900)

if st.button("Predict"):

    input_data = pd.DataFrame([{
        'loan_id': 1,
        'no_of_dependents': dependents,
        'education': 0,
        'self_employed': 0,
        'income_annum': income,
        'loan_amount': loan_amount,
        'loan_term': loan_term,
        'cibil_score': cibil_score,
        'residential_assets_value': 0,
        'commercial_assets_value': 0,
        'luxury_assets_value': 0,
        'bank_asset_value': 0
    }])

    # Prediction (INSIDE BUTTON)
    prediction = model.predict(input_data)[0]
    proba = model.predict_proba(input_data)[0]

    approval_prob = proba[1] * 100

    # Risk logic
    if approval_prob >= 75:
        risk = "Low Risk 🟢"
        recommendation = "Approve Loan"
    elif approval_prob >= 50:
        risk = "Medium Risk 🟠"
        recommendation = "Review Carefully"
    else:
        risk = "High Risk 🔴"
        recommendation = "Reject Loan"

    # Output
    st.subheader("Result Page")

    st.write("### Approval Probability:", f"{approval_prob:.2f}%")
    st.write("### Risk Category:", risk)
    st.write("### Recommendation:", recommendation)

    if prediction == 1:
        st.success("Prediction Outcome: Loan Approved ✅")
    else:
        st.error("Prediction Outcome: Loan Rejected ❌")
