import pandas as pd
import pickle
from sklearn.preprocessing import StandardScaler

# Load your dataset
df = pd.read_csv('heart_failure_clinical_records_dataset (1).csv')

# List all feature columns used for training (exclude target column)
feature_columns = [
    'age',
    'anaemia',
    'creatinine_phosphokinase',
    'diabetes',
    'ejection_fraction',
    'high_blood_pressure',
    'platelets',
    'serum_creatinine',
    'serum_sodium',
    'sex',
    'smoking',
    'time'
]

X = df[feature_columns]

# Fit the scaler
scaler = StandardScaler()
scaler.fit(X)

# Save the scaler
with open('scaler.pkl', 'wb') as f:
    pickle.dump(scaler, f)

print("scaler.pkl created successfully!")