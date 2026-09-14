# Deployment Notes

The Streamlit app depends on the saved model artifacts being available at the repository root.

## Local run

Install the packages from `requirements.txt`, then start the app with:

```bash
streamlit run streamlit_py.py
```

The deployed application uses the same prediction flow as the local version, so changes to preprocessing or feature names should be tested against the saved artifacts before deployment.
