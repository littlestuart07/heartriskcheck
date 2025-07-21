from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)

# Load model and scaler
with open('heart_model.pkl', 'rb') as f:
    model = pickle.load(f)
with open('scaler.pkl', 'rb') as f:
    scaler = pickle.load(f)

@app.route('/', methods=['GET', 'POST'])
def index():
    prediction = None
    values = {}
    if request.method == 'POST':
        try:
            values = request.form.to_dict()
            data = [
                float(values['age']),
                float(values['anaemia']),
                float(values['creatinine_phosphokinase']),
                float(values['diabetes']),
                float(values['ejection_fraction']),
                float(values['high_blood_pressure']),
                float(values['platelets']),
                float(values['serum_creatinine']),
                float(values['serum_sodium']),
                float(values['sex']),
                float(values['smoking']),
                float(values['time'])
            ]
            data_scaled = scaler.transform([data])
            pred = model.predict(data_scaled)[0]
            prediction = "High Risk of Heart Disease" if pred == 1 else "Low Risk of Heart Disease"
        except Exception as e:
            prediction = f"Error: {e}"
    return render_template('index.html', prediction=prediction, values=values)

if __name__ == '__main__':
    app.run(debug=True) 