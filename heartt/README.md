# ❤️ Heart Failure Prediction Project

## 📌 Project Overview

This project uses a Machine Learning model to predict whether a person is likely to suffer from heart disease based on medical data. The model is trained using the Heart Failure Prediction dataset and is deployed as a Flask web application with a clean and responsive frontend.

Our aim is to build a system that can assist healthcare professionals by providing quick risk assessments with high accuracy.

---

## 📊 Dataset Description

- **Source:** [Kaggle - Heart Failure Prediction](https://www.kaggle.com/datasets/fedesoriano/heart-failure-prediction)
- **Rows:** 918
- **Target Variable:** `HeartDisease` (0 = No, 1 = Yes)
- **Features Include:**
  - Age
  - Sex
  - ChestPainType
  - RestingBP
  - Cholesterol
  - FastingBS
  - RestingECG
  - MaxHR
  - ExerciseAngina
  - Oldpeak
  - ST_Slope

---

## 🤖 Model Description

- **Algorithm Used:** XGBoost Classifier
- **Preprocessing:** Standard Scaler
- **Accuracy Achieved:** > 85% on test data
- **Model Files:** 
  - `heart_model.pkl` – Trained ML model
  - `scaler.pkl` – StandardScaler object used for input normalization

---

## 🧪 Installation Instructions

1. Clone the repository:

```bash
git clone https://github.com/your-username/heart-failure-prediction.git
cd heart-failure-prediction
``` 