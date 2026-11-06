import pandas as pd
import random

students = []

for i in range(1, 101):

    cgpa = round(random.uniform(6.0, 9.8), 1)
    aptitude = random.randint(50, 100)
    coding = random.randint(50, 100)
    dsa = random.randint(50, 100)
    communication = random.choice(["Poor", "Average", "Good", "Excellent"])
    internship = random.randint(0, 3)
    projects = random.randint(1, 5)
    certifications = random.randint(0, 6)
    hackathons = random.randint(0, 3)
    resume = random.randint(55, 100)
    mock = random.randint(50, 100)

    # Placement Logic
    score = 0

    if cgpa >= 8.0:
        score += 2

    if aptitude >= 70:
        score += 2

    if coding >= 75:
        score += 2

    if dsa >= 70:
        score += 1

    if communication in ["Good", "Excellent"]:
        score += 1

    if internship >= 1:
        score += 1

    if projects >= 3:
        score += 1

    if certifications >= 2:
        score += 1

    if hackathons >= 1:
        score += 1

    if resume >= 75:
        score += 1

    if mock >= 75:
        score += 1

    if score >= 9:
        placed = "Yes"
    else:
        placed = "No"

    students.append([
        i,
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
        mock,
        placed
    ])

columns = [
    "Student_ID",
    "CGPA",
    "Aptitude",
    "Coding",
    "DSA",
    "Communication",
    "Internship",
    "Projects",
    "Certifications",
    "Hackathons",
    "ResumeScore",
    "MockInterview",
    "Placed"
]

df = pd.DataFrame(students, columns=columns)

df.to_csv("students.csv", index=False)

print("100 student records created successfully!")