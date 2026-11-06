import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

# Read dataset
data = pd.read_csv("students.csv")
print(data.iloc[0])
print(data["Placed"].value_counts())

# Convert text into numbers
data["Communication"] = data["Communication"].map({
    "Poor": 0,
    "Average": 1,
    "Good": 2,
    "Excellent": 3
})

data["Placed"] = data["Placed"].map({
    "No": 0,
    "Yes": 1
})

# Input features (X)
X = data.drop(["Student_ID","Placed"], axis=1)

# Output (Y)
y = data["Placed"]

# Create model
model = DecisionTreeClassifier(random_state=42)

# Train model
model.fit(X, y)
joblib.dump(model, "placement_model.pkl")
print("Model saved successfully!")

print("Model trained successfully!")
# Test Accuracy
print(X.columns)

new_student = [[
    8.5,     # CGPA
    85,      # Aptitude
    90,      # Coding
    88,      # DSA
    3,       # Communication (Excellent)
    2,       # Internship
    4,       # Projects
    5,       # Certifications
    2,       # Hackathons
    90,      # ResumeScore
    92       # MockInterview
]]

prediction = model.predict(new_student)

if prediction[0] == 1:
    print("Prediction: Student will be Placed")
else:
    print("Prediction: Student will NOT be Placed")