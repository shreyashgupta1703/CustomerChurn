# Model Notes

The churn pipeline uses the same feature preparation during training and prediction. Keeping the feature names in one place helps avoid mismatches between the saved model artifacts and the Streamlit inputs.

## Current artifacts

- `model.pkl` — trained classifier
- `scaler.pkl` — fitted feature scaler
- `feature_columns.pkl` — feature order used by the model

These files are loaded by the Streamlit application at prediction time.
