import pandas as pd
import numpy as np
import joblib
import os

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score,precision_score,recall_score,f1_score,confusion_matrix

df = pd.read_csv("dataset/hotel_bookings.csv")

print(df.head())

print(df.shape)

print(df.info())

print(df.isnull().sum())

df.drop_duplicates(inplace=True)
print(df.shape)
df["children"] = df["children"].fillna(0)

df["country"] = df["country"].fillna("Unknown")

df["agent"] = df["agent"].fillna(0)

if "company" in df.columns:
    df.drop(columns=["company"], inplace=True)

df["total_stay"] = df["stays_in_weekend_nights"] + df["stays_in_week_nights"]

df["total_guests"] = df["adults"] + df["children"] + df["babies"]

df["total_cost"] = df["adr"] * df["total_stay"]

df["adr_per_guest"] = df["adr"] / df["total_guests"].replace(0,1)

drop_columns = [

"reservation_status",

"reservation_status_date"

]

for col in drop_columns:

    if col in df.columns:

        df.drop(col,axis=1,inplace=True)

df = pd.get_dummies(df,drop_first=True)
y = df["is_canceled"]

X = df.drop("is_canceled",axis=1)

selected_features = [

"lead_time",

"adr",

"total_stay",

"total_cost",

"adr_per_guest",

"total_of_special_requests",

"arrival_date_day_of_month",

"arrival_date_week_number",

"agent",

"adults"

]

X = X[selected_features]
X_train,X_test,y_train,y_test = train_test_split(

X,

y,

test_size=0.20,

random_state=42,

stratify=y

)

scaler = StandardScaler()

X_train = scaler.fit_transform(X_train)

X_test = scaler.transform(X_test)

model = RandomForestClassifier(

n_estimators=200,

random_state=42

)

model.fit(X_train,y_train)

prediction = model.predict(X_test)

accuracy = accuracy_score(y_test,prediction)

precision = precision_score(y_test,prediction)

recall = recall_score(y_test,prediction)

f1 = f1_score(y_test,prediction)

cm = confusion_matrix(y_test,prediction)

print()

print("Accuracy :",accuracy)

print("Precision :",precision)

print("Recall :",recall)

print("F1 Score :",f1)

print()

print(cm)

os.makedirs("models",exist_ok=True)

joblib.dump(model,"models/model.pkl")

joblib.dump(scaler,"models/scaler.pkl")

joblib.dump(selected_features,"models/feature_columns.pkl")

print()

print("Model Saved Successfully")
