import streamlit as st
import numpy as np
import joblib
import pathlib

# ── 1  load the trained LinearRegression model ────────────────
MODEL_PATH = pathlib.Path(__file__).parent.parent / "models" / "linear.joblib"
model = joblib.load(MODEL_PATH)

# ── 2  Streamlit page settings ─────────────────────────────────
st.set_page_config(page_title="House-Price Estimator", page_icon="🏠")
st.title("🏠 Quick House-Price Estimator")

# ── 3  user-controlled features ───────────────────────────────
area  = st.slider("Living area (sq ft)",           500, 4000, 1500, step=50)
beds  = st.slider("Bedrooms",                      1,   6,    3)
baths = st.slider("Total bathrooms (½ bath = 0.5)", 1.0, 4.5,  2.0, step=0.5)

# ── 4  same feature engineering you used in the notebook ──────
log_area = np.log1p(area)
features = [[log_area, beds, baths]]

# ── 5  predict & display ──────────────────────────────────────
log_pred = model.predict(features)[0]
price    = np.expm1(log_pred)

st.metric("Estimated Sale Price", f"${price:,.0f}")
st.caption("Model: multiple linear regression on log(area), bedrooms, and baths.")
