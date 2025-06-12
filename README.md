_**House Price Estimator**_


_**Overview**_

A user-friendly tool that leverages Multiple Linear Regression to estimate house sale prices from living area and bathroom count. It demonstrates an end-to-end workflow:

1. Data ingestion from Kaggle
2. Exploratory data analysis (EDA)
3. Linear Regression model training
4. Interactive deployment via Streamlit


Dataset: Kaggle House Prices (Advanced Regression Techniques)


_**Features**_

🛠️ Data Ingestion: Load raw CSVs into Pandas DataFrames

🔍 EDA: Histograms, scatterplots, correlation heatmaps to understand data patterns

🔧 Feature Engineering: Create TotalBath; apply log-transform to skewed variables

🔢 Modeling: Fit & evaluate a Multiple Linear Regression (RMSE, R²) baseline

🚀 Deployment: Streamlit app with sliders for real-time price predictions



_**Modeling:**_
* Multiple Linear Regression equation:
predicted_log_price = β₀ + β₁*LogArea + β₂*Bedrooms + β₃*TotalBath

1️⃣ Feature Engineering
Log-transform GrLivArea; combine baths into TotalBath

2️⃣ Split Data
80% train / 20% test

3️⃣ Train Model
Fit using Ordinary Least Squares

4️⃣ Evaluate
Compute RMSE & R²; back-transform RMSE with expm1

5️⃣ Diagnose
Plot Actual vs Predicted, Residuals vs Predicted, Residual histogram

_Provides a transparent, interpretable baseline before trying complex models._



_**Installation Prerequisites:**_
1.Python 3.10+

2.Git

3.Kaggle API token (~/.kaggle/kaggle.json)



_**Usage:**_

*Jupyter Notebooks

1. 01_eda.ipynb: Data overview & visualization
   
2. 02_model.ipynb: Feature engineering, modeling & diagnostics


*Streamlit App

1.streamlit run src/app.py



_**Sturucture:**_

house-price-linear/

├── data/                   # Raw Kaggle CSVs (ignored in Git)

├── models/                 # Saved model artifact (linear.joblib)

├── notebooks/              # Jupyter notebooks for EDA & modeling

├── src/                    # Streamlit app code

├── requirements.txt        # Pinned Python dependencies

└── README.md               # Project documentation



_**Results & Diagnostics:**_

Linear Regression Model

1.RMSE (log-space):0.1567

2.Approx. $ Error:$19,500

3.R²:0.726











🔮 Future Work

1.Test Ridge & Lasso for regularization

2.Add features: location, year built, lot size

3.Containerize with Docker

4.Implement CI/CD & unit tests

Build a dashboard for deeper insights
