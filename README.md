Calories Burn Prediction using Machine Learning

This project presents a machine learning framework to predict calories burned during physical activity using demographic and physiological features. Multiple regression models were evaluated, and the best-performing model was deployed as a web application for real-time predictions.

Overview

Accurate estimation of energy expenditure is important for fitness tracking and health monitoring. Traditional formula-based approaches rely on simplified assumptions and limited variables. This project applies data-driven regression techniques to capture nonlinear relationships and improve predictive accuracy.

Dataset

The dataset contains exercise session records with the following features:

Gender

Age

Height (cm)

Weight (kg)

Duration (minutes)

Heart Rate (bpm)

Body Temperature (°C)

Target variable: Calories Burned

Data was split using an 80/20 train–test ratio.

Methodology

Data preprocessing and encoding

Feature scaling for SVR and KNN

Training and comparison of five regression models:

Ridge Regression

Support Vector Regression (RBF)

K-Nearest Neighbours

Random Forest

XGBoost

Model evaluation using R², MAE, and RMSE

5-fold cross-validation for performance stability

Results

XGBoost achieved the best performance:

R² Score: 0.9988

MAE: 1.48

RMSE: 2.17

5-fold Cross-Validation Mean R²: 0.99889

Deployment

The final model was serialized and integrated into a Flask-based web application.
Users can input exercise parameters and receive real-time calorie predictions through a simple web interface built using HTML, CSS, and JavaScript.

Tech Stack

Python, Pandas, NumPy, Scikit-learn, XGBoost, Flask, HTML, CSS, JavaScript
