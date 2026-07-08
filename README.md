# Credit Risk Analysis System

## Project Overview

The Credit Risk Analysis System is a data science project that predicts whether a loan applicant is likely to be approved or rejected based on financial and personal information. The system uses machine learning algorithms to analyze applicant data, assess credit risk, and generate loan approval recommendations.

## Objectives

- Analyze customer financial data.
- Identify low-risk and high-risk applicants.
- Predict loan approval using machine learning.
- Visualize customer and loan data.
- Develop an interactive dashboard.
- Generate loan approval recommendations.

## Dataset

- **Dataset:** loan_appoval_dataset
- **Source:** Kaggle
- **Number of Records:** 4,269
- **Target Variable:** `loan_status`

The dataset includes information such as:
- Number of Dependents
- Education
- Self Employment Status
- Annual Income
- Loan Amount
- Loan Term
- CIBIL Score
- Residential Asset Value
- Commercial Asset Value
- Luxury Asset Value
- Bank Asset Value

## Technologies Used

- Python
- Google Colab
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- Streamlit
- Joblib

## Machine Learning Models

The following models were trained and evaluated:

- Logistic Regression
- Decision Tree
- Random Forest

The best-performing model was selected for loan approval prediction.

## Project Workflow

1. Dataset Collection
2. Data Cleaning and Preprocessing
3. Exploratory Data Analysis (EDA)
4. Feature Engineering
5. Machine Learning Model Development
6. Model Evaluation
7. Dashboard Development
8. Recommendation System
9. Deployment

## Dashboard Features

The dashboard allows users to:

- Enter applicant information
- Predict loan approval status
- View approval probability
- Display risk category
- Generate loan recommendations

## Project Files

- `Credit_Risk_Analysis.ipynb`
- `app.py`
- `credit_risk_model.pkl`
- `loan_approval_dataset.csv`
- `requirements.txt`
- `README.md`

## How to Run the Project

1. Install the required libraries:

```bash
pip install -r requirements.txt
```

2. Run the Streamlit application:

```bash
streamlit run app.py
```

3. Open the local URL displayed in your browser.

## Results

The machine learning models were evaluated using accuracy, confusion matrix, and classification reports. The best-performing model was selected for the final prediction system and integrated into the Streamlit dashboard.

## Future Scope

- Integration with real-time banking systems
- Training using larger datasets
- Fraud detection
- Credit card risk prediction
- Cloud deployment

## Author

**Changchak Choton**

Bachelor of Computer Applications (BCA)

Data Science Capstone Project