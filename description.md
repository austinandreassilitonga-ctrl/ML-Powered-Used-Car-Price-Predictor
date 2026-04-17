# Used Car Price Prediction

## Repository Outline

```
1. README.md          - General overview of the project
2. notebook.ipynb     - Main notebook for data processing, EDA, and model building
3. notebook_inf.ipynb - Inference notebook to test the final model on new data
4. best_model.pkl     - Saved best model (Stacking: Random Forest + XGBoost + Ridge)
5. deployment/        - Files used for the Streamlit app deployment
```

## Problem Background

Used car companies in India often struggle to set fair market prices for the cars they sell. Pricing is usually done subjectively — based on a salesperson's gut feeling or experience — which can lead to cars being priced too high (hard to sell) or too low (losing profit). This project aims to solve that by building a machine learning model that can predict a used car's price based on its features, so pricing becomes more objective and data-driven.

## Project Output

The output of this project is a machine learning model that can predict the selling price of a used car. The model is also deployed as a web app using Streamlit, so users can input car details and get a price estimate directly.

## Data

The dataset used in this project comes from Kaggle — it contains used car listings from India (sourced from CarDekho). The dataset includes features such as car name, year, fuel type, transmission, mileage, engine capacity, max power, number of seats, and selling price.

## Method

This project uses supervised learning for a regression task. The approach goes through these main steps:

1. **Exploratory Data Analysis (EDA)** — understanding the data distribution, spotting outliers, and finding which features most affect price
2. **Feature Engineering** — handling missing values, removing outliers using Winsorizer, encoding categorical features, scaling numerical features, and creating a new `brand` feature from the car name
3. **Base Modeling** — training and comparing several models: KNN, SVM, Decision Tree, Random Forest, and XGBoost
4. **Stacking** — combining the best two models (Random Forest + XGBoost) with Ridge regression as the final estimator
5. **Hyperparameter Tuning** — using RandomizedSearchCV to find the best parameters for the stacking model

## Stacks

```
pandas==1.5.3
streamlit==1.44.0
numpy==1.26.4
matplotlib==3.7.0
seaborn==0.13.2
plotly==5.9.0
Pillow==11.2.1
scikit-learn==1.6.1
scipy==1.13.1
xgboost==2.14
category_encoders==2.6.4
```

## Reference

- Deployment: https://huggingface.co/spaces/austinsilitonga12/Used_Car-price-predict

---

**Additional References:**
- [Basic Writing and Syntax on Markdown](https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax)
- [README Example 1](https://github.com/fahmimnalfrzki/Swift-XRT-Automation)
- [README Example 2](https://github.com/sanggusti/final_bangkit)
- [How to Write a Good README](https://www.freecodecamp.org/news/how-to-write-a-good-readme-file/)
