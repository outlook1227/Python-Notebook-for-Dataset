# Credit Card Risk Modeling

## Overview
This project develops an **end-to-end credit risk modeling pipeline** to predict the probability of default using machine learning on an imbalanced financial dataset (~30k records).

The workflow includes **feature engineering, model training, evaluation, risk segmentation, and model interpretability**.

---

## Methodology

### Feature Engineering
- Weight of Evidence (**WOE**) transformation  
- Information Value (**IV**) for feature selection  

### Handling Imbalanced Data
- Baseline model
- **SMOTE**
- **Class Weight**

### Machine Learning Models
- Logistic Regression
- Random Forest
- LightGBM
- XGBoost

---

## Model Evaluation

Models were evaluated using metrics commonly used in **credit risk modeling**:

- **AUC**
- **KS Statistic**
- **PSI**
- **Brier Score**
- **Capture Rate**

Best model performance - XGBoost (SMOTE)
Test AUC ≈ 0.88
KS ≈ 0.76


---

## Risk Segmentation
Customers were grouped into **risk bands using decile analysis**:

- Very High Risk
- High Risk
- Medium Risk
- Low Risk
- Very Low Risk

Lift analysis was used to measure model effectiveness in identifying high-risk customers.

---

## Model Interpretability
- Feature importance
- **SHAP values** for explaining model predictions

---

## Tech Stack
Python • Scikit-learn • LightGBM • XGBoost • SHAP • Pandas • NumPy • Matplotlib • Seaborn

---

## Project Workflow
- EDA  
- WOE / IV Feature Engineering  
- Imbalance Handling (SMOTE / Class Weight)  
- Model Training  
- Model Evaluation (AUC / KS / PSI)  
- Risk Segmentation  
- SHAP Interpretability

**Author:** Đỗ Đức Tiến
