# 🧠 Telco Customer Churn Prediction App

👉 **Live App:** [Churn Prediction Streamlit App](https://churn-prediction-app-3rdtimeacharm.streamlit.app/)

Customer churn prediction is a practical machine learning problem where companies identify customers who are likely to stop using their services. Predicting churn can help teams prioritize retention efforts and reduce avoidable revenue loss.

This project uses the **Telco Customer Churn** dataset to build a binary classification model and expose the final prediction pipeline through a Streamlit app.

## App Preview

![App Screenshot](churn1.PNG)

## Dataset

The project uses the publicly available **Telco Customer Churn** dataset sourced from Kaggle / IBM Sample Data.

Dataset: [Telco Customer Churn - Kaggle](https://www.kaggle.com/datasets/blastchar/telco-customer-churn)

The data contains customer demographics, subscribed services, account information, and a churn label.

## ML Workflow

### 1. Data Preprocessing

- Handled missing values in `TotalCharges`.
- Encoded binary categorical features.
- Applied one-hot encoding to multi-class categorical variables.
- Scaled numerical features using `StandardScaler`.

### 2. Model Training

Two classification models were used:

- **Logistic Regression** as a baseline model.
- **Random Forest Classifier** as the final model.

### 3. Model Evaluation

The models were evaluated using:

- Accuracy
- Precision
- Recall
- F1 Score
- ROC-AUC

### 4. Feature Importance

Random Forest feature importance was used to understand which input variables contributed most to the prediction. Important features include factors such as customer tenure, contract type, monthly charges, and payment method.

## Streamlit App

The deployed app loads the trained model, scaler, and feature-column metadata and allows users to enter customer details through an interactive interface.

The app then returns:

- Predicted churn status
- Churn probability

👉 **Live App:** [Churn Prediction Streamlit App](https://churn-prediction-app-3rdtimeacharm.streamlit.app/)

## Deployment

The application can be deployed using Streamlit Community Cloud:

1. Create a Streamlit account.
2. Connect the GitHub repository.
3. Select the repository and `main` branch.
4. Choose `streamlit_py.py` as the application file.
5. Streamlit installs the dependencies from `requirements.txt` and starts the app.

## 🧰 Tech Stack

| Tool | Purpose |
|------|---------|
| Python | Core development |
| pandas, numpy | Data manipulation |
| scikit-learn | Model training and preprocessing |
| joblib | Model artifact loading |
| Streamlit | Interactive prediction app |
| GitHub | Source control |
| Kaggle | Dataset source |

## Performance and Limitations

The dataset contains roughly 7,000 customer records, so model performance may not generalize perfectly to other customer populations or future data distributions.

Predictions should be treated as decision-support signals rather than the sole basis for customer retention decisions. Real-world usage would benefit from monitoring, retraining, and validation on newer customer data.

## Data and Ethics

Customer churn datasets can contain demographic and behavioral patterns that may introduce bias. Predictions should therefore be interpreted with appropriate business context and human oversight.

## Notes

The trained prediction pipeline and Streamlit interface are kept together so the preprocessing steps used during training can be reused when making predictions.
