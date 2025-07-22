# ❤️ Heart Disease Predictor

## 📌 Project Overview
This project is a web application that predicts the risk of heart disease using a machine learning model trained on clinical data. The app features a modern, stylish UI and provides instant predictions based on user input.

## 🚀 Features
- Predicts heart disease risk using 12 clinical features
- Beautiful, responsive, and modern UI
- Two-column input form for easy data entry
- Result display with risk assessment
- Reset button to clear all inputs and results

## 🗂️ Project Structure
```
heartt/
  ├── app.py                # Flask backend
  ├── heart_model.pkl       # Trained ML model
  ├── scaler.pkl            # StandardScaler for input normalization
  ├── heart_failure_clinical_records_dataset (1).csv  # Dataset
  ├── static/
  │     └── style.css       # CSS styles
  ├── templates/
  │     └── index.html      # Main HTML template
  └── README.md             # Project documentation
```

## 🧑‍💻 Installation & Setup

### 1. Clone the repository
```bash
git clone https://github.com/littlestuart07/heartriskcheck.git
cd heartriskcheck
```

### 2. Create a virtual environment (recommended)
```bash
python -m venv venv
# Activate the environment:
# On Windows:
venv\Scripts\activate
# On Mac/Linux:
source venv/bin/activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Prepare the model and scaler
- Ensure `heart_model.pkl` and `scaler.pkl` are present in the project root.
- If not, train your model and scaler using your dataset and save them as `heart_model.pkl` and `scaler.pkl`.

### 5. Run the Flask app
```bash
python app.py
```

### 6. Open the app in your browser
Go to [http://127.0.0.1:5000/](http://127.0.0.1:5000/) to use the web interface.

## 📝 Usage
- Fill in all the clinical features in the form.
- Click **Predict** to see the risk assessment.
- Click **Reset** to clear all fields and results.

## ⚙️ Dependencies
- Flask
- scikit-learn
- numpy
- pandas
- xgboost

All dependencies are listed in `requirements.txt`.

## 📊 Dataset
- [Kaggle - Heart Failure Prediction](https://www.kaggle.com/datasets/fedesoriano/heart-failure-prediction)

## 🤝 Contributing
Pull requests are welcome! For major changes, please open an issue first to discuss what you would like to change.

## 📄 License
This project is licensed under the MIT License.

---

You can copy and paste this content into your `README.md` file! If you want to customize any section, let me know! 
