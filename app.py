from flask import Flask, render_template, request
import joblib
import pandas as pd

app = Flask(__name__)

# Load the trained model
model = joblib.load("placement_model.pkl")
data = pd.read_csv("students.csv")

total_students = len(data)
placed_students = len(data[data["Placed"] == "Yes"])
not_placed_students = len(data[data["Placed"] == "No"])

@app.route("/")
def home():
    return render_template(
    "index.html",
    total=total_students,
    placed=placed_students,
    notplaced=not_placed_students
)

@app.route("/predict", methods=["POST"])
def predict():

    cgpa = float(request.form["cgpa"])
    aptitude = int(request.form["aptitude"])
    coding = int(request.form["coding"])
    dsa = int(request.form["dsa"])
    communication = int(request.form["communication"])
    internship = int(request.form["internship"])
    projects = int(request.form["projects"])
    certifications = int(request.form["certifications"])
    hackathons = int(request.form["hackathons"])
    resume = int(request.form["resume"])
    mock = int(request.form["mock"])

    data = [[
        cgpa,
        aptitude,
        coding,
        dsa,
        communication,
        internship,
        projects,
        certifications,
        hackathons,
        resume,
        mock
    ]]

    print(data)
    prediction = model.predict(data)
    print(prediction)

    if prediction[0] == 1:
        result = "🎉 Student will be Placed"
    else:
        result = "❌ Student will NOT be Placed"
        return render_template(
            "index.html",
             total=100,
             placed=39,
             notplaced=61,
             result=result
      )

    return render_template(
    "result.html",
    result=result,
    cgpa=cgpa,
    aptitude=aptitude,
    coding=coding,
    dsa=dsa,
    communication=communication,
    internship=internship,
    projects=projects,
    certifications=certifications,
    hackathons=hackathons,
    resume=resume,
    mock=mock
)

if __name__ == "__main__":
    app.run(debug=True)