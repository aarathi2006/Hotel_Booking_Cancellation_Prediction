from flask import Flask, render_template, request, redirect, url_for, session, flash
import sqlite3
import numpy as np
from utils.database import connect_db

from utils.helper import hash_password, verify_password

import joblib

app = Flask(__name__)

app.secret_key = "hotel_booking_secret_key"

model = joblib.load("models/model.pkl")
scaler = joblib.load("models/scaler.pkl")
feature_columns = joblib.load("models/feature_columns.pkl")

@app.route("/")
def index():

    if "user_id" in session:
        return redirect(url_for("home"))

    return redirect(url_for("login"))
    

@app.route("/signup", methods=["GET","POST"])

def signup():

    if request.method=="POST":

        fullname=request.form["fullname"]

        email=request.form["email"]

        password=request.form["password"]

        hashed_password=hash_password(password)

        conn=connect_db()

        cursor=conn.cursor()

        try:

            cursor.execute("""
            INSERT INTO users(fullname,email,password)

            VALUES(?,?,?)

            """,(fullname,email,hashed_password))

            conn.commit()

            flash("Registration Successful")

            return redirect(url_for("login"))

        except:

            flash("Email Already Exists")

        finally:

            conn.close()

    return render_template("signup.html")
    
@app.route("/login",methods=["GET","POST"])

def login():

    if request.method=="POST":

        email=request.form["email"]

        password=request.form["password"]

        conn=connect_db()

        cursor=conn.cursor()

        cursor.execute("SELECT * FROM users WHERE email=?",(email,))

        user=cursor.fetchone()

        conn.close()

        if user:

            if verify_password(user["password"],password):

                session["user_id"]=user["id"]

                session["fullname"]=user["fullname"]

                return redirect(url_for("home"))

        flash("Invalid Email or Password")

    return render_template("login.html")
    
@app.route("/home")

def home():

    if "user_id" not in session:

        return redirect(url_for("login"))

    return render_template("home.html",name=session["fullname"])

@app.route("/about")

def about():

    if "user_id" not in session:

        return redirect(url_for("login"))

    return render_template("about.html")


@app.route("/history")
def history():

    if "user_id" not in session:
        return redirect(url_for("login"))

    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT *
        FROM predictions
        WHERE user_id = ?
        ORDER BY created_at DESC
    """, (session["user_id"],))

    history = cursor.fetchall()

    conn.close()

    return render_template("history.html", history=history)
    
    
@app.route("/predict", methods=["GET", "POST"])
def predict():

    if "user_id" not in session:
        return redirect(url_for("login"))

    if request.method == "GET":
        return render_template("predict.html")

    # -----------------------------
    # Get Form Data
    # -----------------------------

    lead_time = int(request.form["lead_time"])

    arrival_day = int(request.form["arrival_day"])

    arrival_week = int(request.form["arrival_week"])

    weekend_nights = int(request.form["weekend_nights"])

    week_nights = int(request.form["week_nights"])

    adr = float(request.form["adr"])

    adults = int(request.form["adults"])

    agent = int(request.form["agent"])

    special_requests = int(request.form["special_requests"])


    # -----------------------------
    # Feature Engineering
    # -----------------------------

    total_stay = weekend_nights + week_nights

    total_cost = total_stay * adr

    adr_per_guest = adr / max(adults, 1)


    # -----------------------------
    # Create Feature Vector
    # -----------------------------

    features = [[

        lead_time,

        adr,

        total_stay,

        total_cost,

        adr_per_guest,

        special_requests,

        arrival_day,

        arrival_week,

        agent,

        adults

    ]]


    # -----------------------------
    # Scaling
    # -----------------------------

    features = scaler.transform(features)


    # -----------------------------
    # Prediction
    # -----------------------------

    prediction = model.predict(features)[0]

    probability = np.max(model.predict_proba(features)) * 100


    if prediction == 1:
        result = "Cancelled"
    else:
        result = "Not Cancelled"


    # -----------------------------
    # Save into Database
    # -----------------------------

    conn = sqlite3.connect("database.db")

    cursor = conn.cursor()

    cursor.execute("""

    INSERT INTO predictions(

    user_id,

    lead_time,

    arrival_date_day_of_month,

    arrival_date_week_number,

    stays_in_weekend_nights,

    stays_in_week_nights,

    adr,

    adults,

    agent,

    total_of_special_requests,

    prediction,

    probability

    )

    VALUES(?,?,?,?,?,?,?,?,?,?,?,?)

    """,(

    session["user_id"],

    lead_time,

    arrival_day,

    arrival_week,

    weekend_nights,

    week_nights,

    adr,

    adults,

    agent,

    special_requests,

    result,

    probability

    ))

    conn.commit()

    conn.close()


    return render_template(

        "result.html",

        prediction=result,

        probability=round(probability,2),

        lead_time=lead_time,

        total_stay=total_stay,

        total_cost=round(total_cost,2),

        adr_per_guest=round(adr_per_guest,2)

    )
    
@app.route("/logout")

def logout():

    session.clear()

    return redirect(url_for("login"))
    
if __name__=="__main__":

    app.run(debug=True)
