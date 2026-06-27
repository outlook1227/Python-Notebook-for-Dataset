## Credit Risk Analysis & Loan Default Prediction at Nova Bank

This project analyzes loan default risk for Nova Bank using Python, Machine Learning, and Power BI. The main objective is to identify high-risk borrower profiles, understand key drivers of loan default, and support data-driven lending decisions.

### 1. Machine Learning Notebook

The Python notebook covers the full credit risk modeling workflow, including data cleaning, exploratory data analysis, feature engineering, leakage detection, model training, evaluation, and interpretation.

Key steps:

* Cleaned and validated a credit risk dataset with 32K+ borrower records.
* Performed EDA to analyze default patterns across income, loan amount, interest rate, debt burden, credit history, and loan purpose.
* Engineered domain-based credit risk features such as loan-to-income ratio, debt-to-income ratio, credit utilization, and risk segments.
* Built and compared multiple models including Logistic Regression, Random Forest, MLP, and LightGBM.
* Evaluated models using ROC-AUC, KS, PSI, Brier Score, Recall, F1-score, and Capture Rate.
* Selected LightGBM with class weighting as the best stable model, achieving strong predictive performance.
* Applied feature importance analysis to explain the main drivers of default risk.

### 2. Power BI Dashboard

The Power BI dashboard provides a business-oriented view of credit risk and borrower segmentation. It is designed to help stakeholders monitor default rates, identify risky borrower groups, and make better lending policy decisions.

Dashboard pages:

* Portfolio Overview: loan default distribution, country-level risk, education profile, and loan grade risk.
* Borrower Profile: age, income group, education level, and marital status analysis.
* Loan Risk Factors: default risk by loan grade, loan purpose, loan amount, interest rate, and loan term.
* Financial Health: borrower affordability analysis using income, loan amount, debt-to-income ratio, and loan-to-income ratio.
* Credit History: default risk by past delinquencies, credit utilization, credit history length, and previous default records.
* Risk Segmentation: borrower distribution across Low, Medium, and High Risk segments with default rate and financial profile comparison.

### Key Insights

* The overall loan default rate is around 21.82%.
* Loan grade, interest rate, loan-to-income ratio, and debt-to-income ratio are major indicators of default risk.
* Borrowers with weaker credit histories and higher credit utilization are more likely to default.
* High-risk borrowers show significantly higher default rates and larger debt burdens.
* Risk segmentation can support differentiated lending strategies such as auto-approval, manual review, or stricter underwriting.

### Tools & Technologies

* Python
* Pandas, NumPy
* Matplotlib, Seaborn
* Scikit-learn
* LightGBM
* Power BI
* SHAP / Feature Importance
* Credit Risk Metrics: ROC-AUC, KS, PSI, Brier Score, Capture Rate

