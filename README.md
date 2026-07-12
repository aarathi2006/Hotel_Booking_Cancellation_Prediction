
# 🏨 AI-Powered Hotel Booking Cancellation Prediction

An end-to-end Machine Learning web application that predicts whether a hotel booking is likely to be cancelled based on booking details. The project is built using **Random Forest**, **Flask**, **SQLite**, **HTML**, **CSS**, and **JavaScript**, providing an interactive and user-friendly interface for prediction and history management.

---

## 📌 Project Overview

Hotel booking cancellations lead to significant financial losses for hotels due to vacant rooms, inefficient resource planning, and reduced revenue. This project aims to predict booking cancellations before check-in using Machine Learning, enabling hotels to take preventive actions and improve occupancy management.

The application allows users to:

- User Registration & Login
- Predict hotel booking cancellations
- Store prediction history
- View previous predictions
- Secure user authentication using SQLite

---

## 🚀 Features

- 🔐 User Registration and Login
- 🤖 AI-based Booking Cancellation Prediction
- 📊 Random Forest Machine Learning Model
- 💾 SQLite Database Integration
- 📜 Prediction History
- 🎨 Responsive Modern User Interface
- 🌐 Flask Web Application
- 📈 Feature Engineering and Data Preprocessing

---

## 🧠 Machine Learning Workflow

- Data Collection
- Data Cleaning
- Feature Engineering
- Train-Test Split
- Model Training
- Model Evaluation
- Model Selection
- Model Serialization (.pkl)
- Flask Deployment

---

## 📂 Project Structure

```
Hotel_Booking_Cancellation_Prediction/
│
├── app.py
├── train_model.py
├── requirements.txt
├── database.db
│
├── models/
│   ├── model.pkl
│   ├── scaler.pkl
│   └── feature_columns.pkl
│
├── dataset/
│   └── hotel_bookings.csv
│
├── static/
│   ├── css/
│   ├── js/
│   ├── images/
│   
│
├── templates/
│   ├── login.html
│   ├── signup.html
│   ├── home.html
│   ├── predict.html
│   ├── result.html
│   ├── history.html
│   ├── about.html
│   └── layout.html
│
└── utils/
    ├── database.py
    └── helper.py
```

---

## 📊 Technologies Used

- Python
- Flask
- SQLite
- HTML5
- CSS3
- JavaScript
- Scikit-learn
- Pandas
- NumPy
- Joblib

---

## 🤖 Machine Learning Algorithm

Multiple machine learning algorithms were compared, including:

- Logistic Regression
- Decision Tree
- Random Forest
- Support Vector Machine
- K-Nearest Neighbors

After evaluation, **Random Forest** achieved the highest accuracy and was selected as the final model.

---

## 📈 Input Features

The prediction model uses the following booking features:

- Lead Time
- Arrival Day of Month
- Arrival Week Number
- Weekend Nights
- Week Nights
- Average Daily Rate (ADR)
- Adults
- Agent ID
- Total Special Requests

Additional engineered features include:

- Total Stay
- Total Cost
- ADR per Guest

---

## 🎯 Output

The model predicts:

- ✅ Not Cancelled
- ❌ Cancelled

along with the prediction probability.

---

## 💻 Installation

Clone the repository

```bash
git clone https://github.com/yourusername/AI-Powered-Hotel-Booking-Cancellation-Prediction.git
```

Go into the project

```bash
cd AI-Powered-Hotel-Booking-Cancellation-Prediction
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the Flask application

```bash
python app.py
```

Open your browser

```
http://127.0.0.1:5000
```

---

## 🌟 Future Enhancements

- Email Notifications
- SMS Alerts
- Cloud Deployment
- Explainable AI (SHAP/LIME)
- Dashboard Analytics
- Mobile Application

---

## 👩‍💻 Author

**Boddu Aarathi**

B.Tech Computer Science and Engineering

Rajiv Gandhi University of Knowledge Technologies (RGUKT)

---

## ⭐ If you found this project useful, don't forget to Star the repository!
