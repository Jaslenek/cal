# Calories Burn Prediction Using Machine Learning

## 1. Project Overview

This project predicts calories burned during physical activity using demographic and physiological inputs.  
Multiple regression models were evaluated, and the best-performing model was deployed as a Flask-based web application for real-time predictions.

---

## 2. Dataset

The dataset contains exercise session records with the following features:

- Gender  
- Age  
- Height (cm)  
- Weight (kg)  
- Duration (minutes)  
- Heart Rate (bpm)  
- Body Temperature (°C)  

**Target Variable:** Calories Burned  

Data split: 80% Training | 20% Testing  

---

## 3. Methodology

### Data Processing
- Data cleaning and encoding
- Feature scaling (for SVR and KNN)

### Models Evaluated
- Ridge Regression
- Support Vector Regression (RBF)
- K-Nearest Neighbours
- Random Forest
- XGBoost

### Evaluation Metrics
- R² Score
- Mean Absolute Error (MAE)
- Root Mean Squared Error (RMSE)
- 5-Fold Cross-Validation

---

## 4. Results

**Best Model: XGBoost**

- R² Score: 0.9988  
- MAE: 1.48  
- RMSE: 2.17  
- Cross-Validation Mean R²: 0.99889  

---

## 5. Deployment

- Backend: Flask  
- Frontend: HTML, CSS, JavaScript  
- Model Serialization: Pickle (.pkl)  
- Real-time prediction via web interface  

---

## 6. Tech Stack

Python  
Pandas  
NumPy  
Scikit-learn  
XGBoost  
Flask  
HTML  
CSS  
JavaScript  

---

## 7. How to Run

```bash
git clone <repository-link>
cd <project-folder>
pip install -r requirements.txt
python app.py
