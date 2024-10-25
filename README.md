# CPI Prediction Model

## Overview
In the pursuit of academic excellence, understanding where you stand can be crucial. This project leverages a **Gradient Boosting Regressor** to predict your Cumulative Performance Index (CPI) based on academic and personal data. By providing key details through a user-friendly web interface, you can receive an accurate estimate of your CPI, helping you gauge your academic performance effectively.

## How It Works

### Model Development
The model predicts CPI using a **Gradient Boosting Regressor**. We expanded a small dataset collected via a Google Form by generating 2000 synthetic entries with **CTGAN** from the **Synthetic Data Vault (SDV)**. Additionally, **Support Vector Regressor (SVR)** was used to create a more comprehensive dataset.

### Exploratory Data Analysis (EDA)
Performed EDA with histograms, scatter plots, heatmaps and boxplots to understand the data. **ANOVA** was used for selecting the most relevant features.

### Data Preprocessing
Applied Ordinal and One-Hot Encoding using a **ColumnTransformer** to prepare the data for modeling.

### Model Optimization
Fine-tuned the Gradient Boosting Regressor, achieving an **R² score** of **0.80** through **Hyperparameter tuning** and **cross-validation**.

### Deployment
Deployed the model using **Flask** on **Azure** and **Render**, offering an intuitive web application for CPI prediction.
 

## How to Use

1. **Visit the Application:** [**CPI Prediction**](cpi-predictor-g3brcfdcece8a3g4.southeastasia-01.azurewebsites.net), and if this link doesn't work then [Click Here](https://cpi-predicition-2.onrender.com/)
3. **Input Data:** Complete the form with your academic and personal information.
4. **Submit:** Send your data for analysis.
5. **Get Prediction:** Receive an estimated CPI based on your inputs.

## Features

- **Gradient Boosting Regressor:** Employs advanced machine learning techniques for accurate CPI forecasts.
- **Synthetic Data Integration:** Enhanced the model with synthetic data for a robust analysis.
- **User-Friendly Interface:** Simple form designed to capture essential details and provide quick predictions.
- **Data-Driven:** Built on a robust dataset that combines real and synthetic data to ensure comprehensive and accurate predictions across various academic profiles.

## Example Output
After submitting your details, the model might provide an estimated CPI like 7.5 or 8.2, depending on your academic performance and personal data. This estimate helps you understand your current academic standing and potential areas for improvement.
