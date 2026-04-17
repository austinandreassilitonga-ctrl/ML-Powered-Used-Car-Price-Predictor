# Used Car Price Prediction

A machine learning project to help used car companies in India set fair and objective prices for the cars they sell — using data, not guesswork.

---

## Problem Background

Used car dealerships often struggle with pricing. Without a clear reference, prices tend to be set subjectively, which can result in cars being overpriced (leading to slow sales) or underpriced (reducing profit). This project builds a predictive model that estimates a used car's market price based on its features, helping companies make more informed and data-driven pricing decisions.

---

## Project Output

- A machine learning model that predicts used car selling prices in Indian Rupee (INR)
- A deployed web application built with Streamlit where users can input car details and get a price estimate

**URL Deployment :** [Used Car Price Predictor](https://huggingface.co/spaces/austinsilitonga12/Used_Car-price-predict)

---

## Repository Structure

```
├── README.md             # Project overview (this file)
├── notebook.ipynb        # Main notebook: EDA, feature engineering, modeling
├── notebook_inf.ipynb    # Inference notebook: testing the model on new data
├── best_model.pkl        # Saved best model
├── description.md        # Project description template
├── conceptual.txt        # Conceptual Q&A about the methods used
└── deployment/           # Streamlit app deployment files
```

---

## Dataset

- **Source:** [Kaggle — Car Price Prediction Dataset](https://www.kaggle.com/datasets/sukhmandeepsinghbrar/car-price-prediction-dataset)
- **Coverage:** Used car listings in India
- **Features:** Car name, year, fuel type, seller type, transmission, ownership history, mileage, engine capacity, max power, number of seats, and selling price

---

## Methods

### 1. Exploratory Data Analysis (EDA)
- Analyzed price distribution, which is heavily right-skewed with several extreme outliers
- Found that year, engine capacity, and max power are the most correlated features with price
- Diesel cars tend to be priced higher than petrol cars
- Most listings use manual transmission

### 2. Feature Engineering
- Extracted `brand` from the car name column to reduce cardinality
- Handled missing values using median imputation
- Capped outliers using Winsorizer (IQR method)
- Applied feature selection using Spearman and Kendall correlation tests
- Encoded categorical features: OneHotEncoder, OrdinalEncoder, and TargetEncoder
- Scaled numerical features using RobustScaler
- Applied log transformation on the target variable to reduce skewness

### 3. Modeling
- Trained and compared 5 base models: KNN, SVM, Decision Tree, Random Forest, XGBoost
- Combined the two best models (Random Forest + XGBoost) using **Stacking** with Ridge regression as the final estimator
- Applied **RandomizedSearchCV** for hyperparameter tuning (50 iterations, 5-fold CV)

---

## Model Performance (Best Model — Stacked + Tuned)

| Metric | Train | Test |
|--------|-------|------|
| R² Score | — | ~0.83 |
| MAE | — | lower than base |
| MAPE | — | lower than base |
| CV Std | — | lower than base |

> The stacking approach combined the accuracy of XGBoost with the stability of Random Forest, resulting in better overall performance and reduced overfitting compared to either model alone.

---

## Business Recommendations

Based on the model results, here are some actionable insights for the business:

- **Objective pricing tool** — Integrate this model into the seller onboarding flow to automatically suggest a price range based on car details
- **Prioritize data completeness** — Year, engine capacity, and max power are critical features; always require these fields to be filled in listings
- **Manual review for premium cars** — The model is most accurate for mid-to-low priced cars; luxury cars (above 1.5M Rupee) may need expert review
- **Leverage fuel type as a filter** — Diesel cars are consistently priced higher, which can be used as a search/filter feature for buyers
- **Highlight ownership history** — First-owner cars can be marketed as premium listings since ownership history impacts price
- **Retrain periodically** — Car market prices shift over time; retraining every 6 months with new data is recommended

---

## Tech Stack

| Library | Version |
|---------|---------|
| pandas | 1.5.3 |
| numpy | 1.26.4 |
| scikit-learn | 1.6.1 |
| xgboost | 2.14 |
| category_encoders | 2.6.4 |
| matplotlib | 3.7.0 |
| seaborn | 0.13.2 |
| plotly | 5.9.0 |
| scipy | 1.13.1 |
| streamlit | 1.44.0 |
| Pillow | 11.2.1 |

---

## Author

**Austin Andreas Ezra Silitonga**

---

## References

- [Kaggle Dataset - Car Price Prediction Dataset](https://www.kaggle.com/datasets/sukhmandeepsinghbrar/car-price-prediction-dataset)
- [Scikit-learn Documentation](https://scikit-learn.org/)
- [XGBoost Documentation](https://xgboost.readthedocs.io/)
- [How to Write a Good README](https://www.freecodecamp.org/news/how-to-write-a-good-readme-file/)
